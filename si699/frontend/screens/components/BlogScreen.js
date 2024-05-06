import React, { useEffect, useState } from 'react';
import { View, ScrollView, StyleSheet, TextInput, Pressable } from 'react-native';
import { FontAwesome } from '@expo/vector-icons';
import BlogBlock from './BlogBlock';
import DropDownPicker from 'react-native-dropdown-picker';
import { useDispatch, useSelector } from 'react-redux';
import { searchByKeywords } from '../../features/resources/resourcesSlice';
DropDownPicker.setMode("BADGE");


const blogs = [
  {
    id: 1,
    title: 'Blog 1',
    author: 'Author 1',
    summary: 'Summary of Blog 1',
    image: require('../../assets/splash.png'),
    tags: ['Tag 1']
  },
  {
    id: 2,
    title: 'Blog 2',
    author: 'Author 2',
    summary: 'Summary of Blog 2',
    image: require('../../assets/splash.png'),
    tags: ['Tag 2']
  },
  {
    id: 3,
    title: 'Blog 3',
    author: 'Author 3',
    summary: 'Summary of Blog 3',
    image: require('../../assets/splash.png'),
    tags: ['Tag 3']
  },
  // Add more blog objects as needed
];

export default function BlogScreen({ route, navigation }) {
  const [searchKey, setSearchKey] = useState()
  const [showFilter, setShowFilter] = useState(false)
  const [selectedTags, setSelectedTags] = useState([]);
  const [tags, setTags] = useState([
    { label: 'Tag 1', value: 'tag1' },
    { label: 'Tag 2', value: 'tag2' }
  ]);

  useEffect(() => navigation.setOptions({ title: route.params.title }))
  // const blogs = useSelector(state => state.blogs)
  // const dispatch = useDispatch()
  // useEffect(() => { dispatch(searchByKeywords()) }, [dispatch])

  return (
    <View>
      <View style={{ paddingVertical: 10, paddingHorizontal: 40, flexDirection: 'row', gap: 20, position: 'relative', zIndex: 4, alignItems: 'center' }}>
        <TextInput
          value={searchKey}
          onChangeText={setSearchKey}
          style={styles.searchBar}
          placeholder='Search'
          returnKeyType='search'
        />

        <Pressable>
          <FontAwesome name="filter" size={24} color="black" onPress={() => {
            setShowFilter(!showFilter)
          }} />
        </Pressable>
        {showFilter && <DropDownPicker
          multiple={true}
          min={0}
          max={2}
          open={showFilter}
          value={selectedTags}
          items={tags}
          setOpen={setShowFilter}
          setValue={setSelectedTags}
          setItems={setTags}
          extendableBadgeContainer={true}
          showBadgeDot={false}
          placeholder='Filter by tags'
          containerStyle={{
            position: 'absolute', top: 60, right: 40
          }}
        />
        }
      </View>
      <ScrollView contentContainerStyle={styles.container}>
        {blogs.map((blog) => (
          <BlogBlock key={blog.id} blog={blog} />
        ))}
      </ScrollView>
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    justifyContent: 'flex-start',
    alignItems: 'center',
    paddingBottom: 100
  },
  searchBar: {
    padding: 15,
    borderColor: '#000',
    borderWidth: 1,
    borderRadius: 50,
    flexGrow: 1
  }
});