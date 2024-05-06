import axios from "axios";
import * as Device from 'expo-device';
import { Platform } from 'react-native';
import { BASE_URL } from './Secret';

let baseURL;

// Check if running on a physical device (both iOS and Android)
if (Device.isDevice) {
    baseURL = BASE_URL; // Use BASE_URL for physical iOS and Android devices
} else {
    // Running on a simulator or emulator
    if (Platform.OS === 'ios') {
        baseURL = 'http://localhost:3000'; // Use localhost for iOS simulator
    } else if (Platform.OS === 'android') {
        baseURL = 'http://10.0.2.2:3000'; // Use 10.0.2.2 for Android emulator
    }
}

const customAxios = axios.create({
    baseURL,
    withCredentials: true
});
axios.defaults.withCredentials = true;

export default customAxios