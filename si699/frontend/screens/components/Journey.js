import React from 'react';
import { View, Text, FlatList, StyleSheet } from 'react-native';

const Journey = ({ events }) => {
  // Sort events by anti-chronological order
  const sortedEvents = events.sort((a, b) => new Date(b.date) - new Date(a.date));

  // Calculate the number of days between the first and last events
  const firstEventDate = new Date(sortedEvents[sortedEvents.length - 1].date);
  const lastEventDate = new Date(sortedEvents[0].date);
  const numberOfDays = Math.ceil((lastEventDate - firstEventDate) / (1000 * 60 * 60 * 24));

  // Render each event item
  const renderItem = ({ item, index }) => (
    <View style={styles.item}>
      <View style={styles.timelineDot} />
      <View style={styles.content}>
        <Text style={styles.date}>{item.date}</Text>
        <Text style={styles.event}>{item.event}</Text>
      </View>
      {index !== sortedEvents.length - 1 && <View style={styles.connector} />}
    </View>
  );

  const renderUpcomingItem = ({ item, index }) => (
    <View style={styles.item}>
      <View style={styles.timelineDotUpcoming} />
      <View style={styles.upcomingContent}>
        <Text style={styles.event}>{item.event}</Text>
      </View>
      {index !== sortedEvents.length - 1 && <View style={styles.connectorUpcoming} />}
    </View>
  );

  return (
    <View style={styles.container}>
      <View style={styles.headerContainer}>
        <Text style={styles.header}>
          <Text style={styles.numberOfDays}>{numberOfDays}</Text> days of resilience and strength - we're with you every step of the way!
        </Text>
      </View>
      <FlatList
        data={sortedEvents.slice(0, 3)}
        renderItem={renderItem}
        keyExtractor={(item, index) => index.toString()}
        contentContainerStyle={styles.listContent}
      />
      <View style={styles.headerContainer}>
        <Text style={styles.inlineText}>
          You might be experiencing this soon...
        </Text>
      </View>
      <FlatList
        data={events.slice(-3, -1)}
        renderItem={renderUpcomingItem}
        keyExtractor={(item, index) => index.toString()}
        contentContainerStyle={styles.listContent}
      />
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    paddingHorizontal: 20,
    paddingTop: 10,
  },
  headerContainer: {
    alignItems: 'center',
    marginVertical: 20,
  },
  header: {
    fontSize: 20,
    fontWeight: 'bold',
    textAlign: 'center',
  },
  inlineText: {
    fontSize: 16,
    textAlign: 'left',
  },
  numberOfDays: {
    fontSize: 24, 
    fontWeight: 'bold',
    color: '#007bff',
  },
  listContent: {
    paddingBottom: 20,
  },
  item: {
    flexDirection: 'row',
    marginBottom: 20,
    position: 'relative',
  },
  timelineDot: {
    width: 16,
    height: 16,
    borderRadius: 8,
    backgroundColor: '#007bff',
    marginRight: 15,
    marginTop: 4,
  },
  timelineDotUpcoming: {
    width: 16,
    height: 16,
    borderRadius: 8,
    backgroundColor: '#C7CCCE',
    marginRight: 15,
    marginTop: 4,
  },
  content: {
    flex: 1,
    paddingVertical: 10,
    paddingHorizontal: 15,
    borderRadius: 8,
    backgroundColor: 'lightblue',
    borderColor: '#ccc',
    borderWidth: 1,
  },
  upcomingContent: {
    flex: 1,
    paddingVertical: 10,
    paddingHorizontal: 15,
    borderRadius: 8,
    backgroundColor: '#C7CCCE',
    borderColor: '#ccc',
    borderWidth: 1,
  },
  date: {
    fontWeight: 'bold',
    fontSize: 16,
    marginBottom: 5,
  },
  event: {
    fontSize: 16,
  },
  connector: {
    position: 'absolute',
    top: 8,
    bottom: 0,
    left: 7,
    width: 2,
    backgroundColor: '#007bff',
    zIndex: -1,
  },
  connectorUpcoming: {
    position: 'absolute',
    top: 8,
    bottom: 0,
    left: 7,
    width: 2,
    backgroundColor: '#C7CCCE',
    zIndex: -1,
  },
});

export default Journey;
