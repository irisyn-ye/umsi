import {
    getAuth, signInWithEmailAndPassword,
    createUserWithEmailAndPassword,
    updateProfile,
    signOut as fbSignOut,
    initializeAuth,
    getReactNativePersistence,
    onAuthStateChanged,
} from 'firebase/auth';
import { getApps, initializeApp } from 'firebase/app';
import { firebaseConfig } from './Secrets';
import ReactNativeAsyncStorage from '@react-native-async-storage/async-storage';

let app, auth;

// this guards against initializing more than one "App"
const apps = getApps();
if (apps.length == 0) {
    app = initializeApp(firebaseConfig);
} else {
    app = apps[0];
}

// for auto logging in
try {
    auth = initializeAuth(app, {
        persistence: getReactNativePersistence(ReactNativeAsyncStorage)
    });
} catch (error) {
    auth = getAuth(app); // if auth already initialized
}

// get current user to utilize their specific info
const getAuthUser = () => {
    return auth.currentUser;
}

// signing in, up, out
const signIn = async (email, password) => {
    await signInWithEmailAndPassword(auth, email, password);
}

const signUp = async (displayName, email, password) => {
    const userCred = await createUserWithEmailAndPassword(auth, email, password);
    await updateProfile(userCred.user, { displayName: displayName });
}

const signOut = async () => {
    await fbSignOut(auth);
}

// for auto logging in
let unsubscribeFromAuthChanges = undefined;

const subscribeToAuthChanges = (onAuthStateChangedCallback) => {
    if (unsubscribeFromAuthChanges) {
        unsubscribeFromAuthChanges();
    }

    unsubscribeFromAuthChanges = onAuthStateChanged(auth, (user) => {
        if (user) {
            console.log('signed in! user:', user);
            // Pass the entire user object to the callback
            onAuthStateChangedCallback(user);
        } else {
            console.log('user is signed out!');
            // Pass null when there is no user
            onAuthStateChangedCallback(null);
        }
    });
}


export { signIn, signOut, signUp, getAuthUser, subscribeToAuthChanges }