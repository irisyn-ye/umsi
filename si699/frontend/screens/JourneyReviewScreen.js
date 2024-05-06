import React from 'react';
import { View, StyleSheet } from 'react-native';
import Journey from './components/Journey';

const JourneyReviewScreen = () => {
  // Sample events data
  const events = [
    { date: '2024-02-26', event: 'I’m considering or planning to visit' },
    { date: '2024-02-27', event: 'I’ve arrived at the hospital' },
    { date: '2024-02-28', event: 'Meeting with care team' },
    { date: '2024-03-03', event: 'Waiting for answers' },
    { date: '2024-03-17', event: 'Planning for discharge from hospital' },
    // Events should come from assessment question 3
  ];

  return (
    <View style={styles.container}>
      <Journey events={events} />
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#fff',
  },
});

export default JourneyReviewScreen;