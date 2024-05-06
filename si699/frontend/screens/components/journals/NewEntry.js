import React, { useState } from 'react';
import { View, TextInput, Button, Text, StyleSheet } from 'react-native';
import { useNavigation } from '@react-navigation/native';
import { useDispatch } from 'react-redux';
import { createJournalEntry } from '../../../features/journalSlice';
import promptList from './promptArray';

export default function NewEntry({ route }) {
  const { promptId } = route.params;
  const [title, setTitle] = useState(''); 
  const [entryText, setEntryText] = useState('');
  const dispatch = useDispatch();
  const navigation = useNavigation()

  const prompts = promptList;
  const prompt = prompts.find((p) => p.id === promptId);

  const handleSaveEntry = () => {
    const entryData = {
      title: title,          
      text: entryText,
      promptId: promptId,
      promptText: prompt ? prompt.prompt : '',
      entryId: Date.now(),
    };

    dispatch(createJournalEntry(entryData));
    navigation.navigate('Journals')
  };

  return (
    <View style={styles.container}>
      <Text style={{fontSize: 16}}>{prompt ? prompt.prompt : 'Prompt not found'}</Text>
      
      <TextInput 
        placeholder="Title of your Journal Entry"
        value={title}
        onChangeText={setTitle}
        style={styles.titleInput}
      />
      
      <TextInput 
        multiline
        placeholder="Write your journal entry..."
        value={entryText}
        onChangeText={setEntryText}
        style={styles.textInput}
      />
      
      <Button title="Save Entry" onPress={handleSaveEntry} />
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    padding: "5%",
  },
  titleInput: {
    marginBottom: 20,
    borderWidth: 1,
    borderColor: '#ddd',
    padding: 10,
    fontSize: 18,
    borderRadius: 6,
  },
  textInput: {
    flex: 0.9, 
    marginBottom: 20,
    borderWidth: 1,
    borderColor: '#ddd',
    padding: 10,
    fontSize: 18,
    borderRadius: 6,
  },
  button: {
    backgroundColor: 'lightblue',
    padding: 15,
    marginBottom: 10,
    borderRadius: 10,
  },
})
