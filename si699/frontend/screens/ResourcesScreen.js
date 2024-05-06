import React from 'react';
import { View, Text, ScrollView, Image, StyleSheet } from 'react-native';
import { TouchableOpacity } from 'react-native-gesture-handler';
import BlogBlock from './components/BlogBlock';

const Module = ({ title, img, navigation }) => {
  return (
    <TouchableOpacity onPress={() => navigation.navigate('BlogScreen', { title: title })} style={styles.module}>
      <Image src={img} alt="module picture" />
      <Text style={{ flexGrow: 1 }}>{title}</Text>
    </TouchableOpacity>
  )
}

const exampleBlog =
{
  id: 1,
  title: 'Blog 1',
  author: 'Author 1',
  summary: 'Summary of Blog 1',
  image: require('../assets/splash.png'),
  tags: ['Tag 1']
}

export default function ResourcesScreen({ navigation }) {
  return (
    <View style={styles.container}>
      <Text style={styles.title}>Recommended Contents</Text>
      <BlogBlock blog={exampleBlog} />
      <Module title="Self-care and patient care" navigation={navigation} />
      <Module title="Communicating with family and the care team" navigation={navigation} />
      <Module title="Organization support and planning for the future" navigation={navigation} />
    </View>
  )
}

const styles = StyleSheet.create({
  container: {
    flexGrow: 1,
    justifyContent: 'center',
    alignItems: 'center',
  },
  module: {
    backgroundColor: 'lightblue',
    padding: 15,
    marginBottom: 10,
    borderRadius: 10,
    alignItems: 'center',
    flexDirection: 'row',
    width: '80%'
  },
  title: {
    fontSize: 24,
    fontWeight: 600,
    marginTop: 20,
    marginBottom: 10
  }
})
