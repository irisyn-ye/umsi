import { useState, useEffect } from 'react';
import { signIn, signUp, subscribeToAuthChanges } from '../AuthManager';
import { View, Text, TextInput, StyleSheet, Alert } from 'react-native';
import { Button } from '@rneui/themed';
import { useNavigation } from '@react-navigation/native';

// components such as sign in and sign up boxes------------

function SigninBox({ navigation }) {
    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');

    return (
        <View style={styles.loginContainer}>
            <Text style={styles.loginHeaderText}>Sign In</Text>
            <View style={styles.loginRow}>
                <View style={styles.loginLabelContainer}>
                    <Text style={styles.loginLabelText}>Email: </Text>
                </View>
                <View style={styles.loginInputContainer}>
                    <TextInput
                        style={styles.loginInputBox}
                        placeholder='enter email address'
                        autoCapitalize='none'
                        spellCheck={false}
                        onChangeText={text => setEmail(text)}
                        value={email}
                    />
                </View>
            </View>
            <View style={styles.loginRow}>
                <View style={styles.loginLabelContainer}>
                    <Text style={styles.loginLabelText}>Password: </Text>
                </View>
                <View style={styles.loginInputContainer}>
                    <TextInput
                        style={styles.loginInputBox}
                        placeholder='enter password'
                        autoCapitalize='none'
                        spellCheck={false}
                        secureTextEntry={true}
                        onChangeText={text => setPassword(text)}
                        value={password}
                    />
                </View>
            </View>
            <View style={styles.loginRow}>
                <Button
                    onPress={async () => {
                        try {
                            await signIn(email, password);
                        } catch (error) {
                            Alert.alert("Invalid email or password", "Please double check your credentials", [{ text: "Try again" }])
                        }
                    }}
                >
                    Sign In
                </Button>
            </View>
        </View>
    );
}


function SignupBox({ navigation }) {
    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');
    const [displayName, setDisplayName] = useState('');

    return (
        <View style={styles.loginContainer}>
            <Text style={styles.loginHeaderText}>Sign Up</Text>
            <View style={styles.loginRow}>
                <View style={styles.loginLabelContainer}>
                    <Text style={styles.loginLabelText}>Display Name: </Text>
                </View>
                <View style={styles.loginInputContainer}>
                    <TextInput
                        style={styles.loginInputBox}
                        placeholder='enter display name'
                        autoCapitalize='none'
                        spellCheck={false}
                        onChangeText={text => setDisplayName(text)}
                        value={displayName}
                    />
                </View>
            </View>
            <View style={styles.loginRow}>
                <View style={styles.loginLabelContainer}>
                    <Text style={styles.loginLabelText}>Email: </Text>
                </View>
                <View style={styles.loginInputContainer}>
                    <TextInput
                        style={styles.loginInputBox}
                        placeholder='enter email address'
                        autoCapitalize='none'
                        spellCheck={false}
                        onChangeText={text => setEmail(text)}
                        value={email}
                    />
                </View>
            </View>
            <View style={styles.loginRow}>
                <View style={styles.loginLabelContainer}>
                    <Text style={styles.loginLabelText}>Password: </Text>
                </View>
                <View style={styles.loginInputContainer}>
                    <TextInput
                        style={styles.loginInputBox}
                        placeholder='enter password'
                        autoCapitalize='none'
                        spellCheck={false}
                        secureTextEntry={true}
                        onChangeText={text => setPassword(text)}
                        value={password}
                    />
                </View>
            </View>
            <View style={styles.loginRow}>
                <Button
                    onPress={async () => {

                        try {
                            await signUp(displayName, email, password);
                            navigation.navigate("Assessment")
                        } catch (error) {
                            Alert.alert("Sign Up Error", "Invalid email or email already in use.", [{ text: "OK" }])
                        }
                    }}
                >
                    Sign Up
                </Button>
            </View>
        </View>
    );
}

// components end -----------------------------------------

function LoginScreen({ navigation }) {
    const [loginMode, setLoginMode] = useState(true);
    
    useEffect(() => {
        const handleAuthChange = (user) => {
            if (user) {
                if (user.newUser) {
                    // Navigate to Assessment if it's a new user
                    navigation.navigate('Assessment');
                } else {
                    // Navigate to HomeStack if it's an existing user
                    navigation.navigate('HomeStack');
                }
            } else {
                // Navigate to Login if no user is logged in
                navigation.navigate('Login');
            }
        };

        const unsubscribe = subscribeToAuthChanges(handleAuthChange);
        return () => unsubscribe();  
    }, []);

    return (
        <View style={styles.container}>
            <View style={styles.bodyContainer}>

                {loginMode ?
                    <SigninBox navigation={navigation} />
                    :
                    <SignupBox navigation={navigation} />
                }
            </View>
            <View styles={styles.modeSwitchContainer}>
                {loginMode ?
                    <Text>New user?
                        <Text
                            onPress={() => { setLoginMode(!loginMode) }}
                            style={{ color: 'blue' }}> Sign up </Text>
                        instead!
                    </Text>
                    :
                    <Text>Returning user?
                        <Text
                            onPress={() => { setLoginMode(!loginMode) }}
                            style={{ color: 'blue' }}> Sign in </Text>
                        instead!
                    </Text>
                }
            </View>
        </View>
    );
}


const styles = StyleSheet.create({
    container: {
        flex: 1,
        backgroundColor: '#fff',
        alignItems: 'center',
        justifyContent: 'center',
    },
    bodyContainer: {
        flex: 0.5,
        justifyContent: 'center',
        alignItems: 'center',
    },
    loginContainer: {
        flex: 1,
        justifyContent: 'flex-start',
        alignItems: 'center',
        width: '100%',
        paddingTop: '10%',
        paddingBottom: '10%',
    },
    loginHeader: {
        width: '100%',
        padding: '3%',
        justifyContent: 'center',
        alignItems: 'center',
    },
    loginHeaderText: {
        fontSize: 24,
        color: 'black',
        paddingBottom: '5%'
    },
    loginRow: {
        flexDirection: 'row',
        justifyContent: 'flex-start',
        alignItems: 'center',
        width: '100%',
        padding: '3%'
    },
    loginLabelContainer: {
        flex: 0.3,
        justifyContent: 'center',
        alignItems: 'flex-end'
    },
    loginLabelText: {
        fontSize: 18
    },
    loginInputContainer: {
        flex: 0.5,
        justifyContent: 'center',
        alignItems: 'flex-start',
        width: '100%'
    },
    loginInputBox: {
        width: '100%',
        borderColor: 'lightgray',
        borderWidth: 1,
        borderRadius: 6,
        fontSize: 18,
        padding: '2%'
    },
    modeSwitchContainer: {
        flex: 0.2,
        justifyContent: 'center',
        alignItems: 'center',
        width: '100%',
        backgroundColor: 'pink'
    },
    loginButtonRow: {
        width: '100%',
        justifyContent: 'center',
        alignItems: 'center'
    },
    listContainer: {
        flex: 0.7,
        backgroundColor: '#ccc',
        alignItems: 'center',
        justifyContent: 'center',
        width: '100%',
    },
});
export default LoginScreen;