import React from 'react';
import { View, Text, TouchableOpacity, StyleSheet, Alert, Image } from 'react-native';
import { FontAwesome } from '@expo/vector-icons';
import { useNavigation } from '@react-navigation/native';
import { getAuthUser, signOut } from '../AuthManager';

const checkInImage = require('../assets/check-in.jpeg');
const guidedJournalsImage = require('../assets/journal.jpeg');
const resourcesLibraryImage = require('../assets/resources-library.jpeg');
const journeyOverviewImage = require('../assets/journey.jpeg');

export default function HomeScreen({ navigation }) {
  const handleResourcesLibraryPress = () => {
    navigation.navigate('Resources');
  }

  return (
    <View style={styles.container}>
      {/* Profile button */}
      <TouchableOpacity style={styles.profileButton}>
        <FontAwesome name="user-circle" size={24} color="black" />
      </TouchableOpacity>

      {/* Heading */}
      <Text style={styles.heading}>Welcome, {getAuthUser().displayName} 👋</Text>

      {/* Four buttons */}
      <View style={styles.buttonsContainer}>
        <TouchableOpacity style={[styles.button, styles.firstButton]} onPress={() => navigation.navigate('Assessment')}>
          <Image source={checkInImage} style={styles.buttonImage} />
          <Text style={styles.buttonText}>Check in now</Text>
        </TouchableOpacity>
        <TouchableOpacity style={styles.button} onPress={() => navigation.navigate('Journals')}>
          <Image source={guidedJournalsImage} style={styles.buttonImage} />
          <Text style={styles.buttonText}>Guided Journals</Text>
        </TouchableOpacity>
        <View style={styles.horizontalButtonsContainer}>
          <TouchableOpacity style={[styles.button, styles.horizontalButton, styles.leftBottomButton]} onPress={handleResourcesLibraryPress}>
            <Image source={resourcesLibraryImage} style={styles.bottomButtonImage} />
            <Text style={styles.bottomButtonText}>Resources Library</Text>
          </TouchableOpacity>
          <TouchableOpacity style={[styles.button, styles.horizontalButton, styles.rightBottomButton]} onPress={() => navigation.navigate('Journey Overview')}>
            <Image source={journeyOverviewImage} style={styles.bottomButtonImage} />
            <Text style={styles.bottomButtonText}>My Journey Overview</Text>
          </TouchableOpacity>
        </View>
      </View>
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    paddingHorizontal: 20,
    paddingTop: 50,
  },
  profileButton: {
    position: 'absolute',
    top: 20,
    right: 20,
    zIndex: 1,
  },
  heading: {
    fontSize: 20,
    fontWeight: 'bold',
    textAlign: 'left',
    marginBottom: 20,
  },
  buttonsContainer: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
  },
  button: {
    width: 350,
    margin: 10,
    borderRadius: 10,
    alignItems: 'center',
    padding: 15,
    backgroundColor: 'lightblue',
    flexDirection: 'row',
  },
  firstButton: {
    marginTop: 10,
    height: 215,
    justifyContent: 'center',
  },
  buttonText: {
    fontSize: 20,
    fontWeight: 'bold',
    marginLeft: 10,
    textAlign: 'center',
  },
  bottomButtonText: {
    fontSize: 14,
    fontWeight: 'bold',
    marginLeft: 10,
    textAlign: 'center',
  },
  horizontalButtonsContainer: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    marginLeft: 20,
    marginRight: 20,
  },
  horizontalButton: {
    width: 150,
    height: 130,
    backgroundColor: 'lightblue',
    alignItems: 'center',
    justifyContent: 'center',
    flexDirection: 'column',
  },
  leftBottomButton: {
    alignSelf: 'flex-start',
    margin: 20,
  },
  rightBottomButton: {
    alignSelf: 'flex-end',
    margin: 20,
  },
  buttonImage: {
    height: 120,
    width: 120,
    resizeMode: 'contain',
  },
  bottomButtonImage: {
    height: 90,
    width: 90,
    resizeMode: 'contain',
  },
});
