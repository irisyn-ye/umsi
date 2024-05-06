import React, { useState } from 'react';
import { View, Text, TextInput, Button, StyleSheet } from 'react-native';
import { useDispatch } from 'react-redux';
import { updateJournalEntry } from '../../../features/journalSlice';

export default function EditJournalEntry({ route, navigation }) {
  const { entryId, title, text, promptId, promptText } = route.params;

  const [formTitle, setFormTitle] = useState(title);
  const [formText, setFormText] = useState(text);
  const dispatch = useDispatch();

  const handleSave = () => {
    const updatedData = {
      entryId,
      title: formTitle,
      text: formText,
      promptId,
      promptText,
    };

    dispatch(updateJournalEntry(updatedData));
    navigation.navigate("Journal Details", updatedData);
  };

  return (
    <View style={styles.container}>
      <Text style={{ fontSize: 16 }}>Prompt: {promptText}</Text>
      <TextInput
        style={styles.input}
        value={formTitle}
        onChangeText={setFormTitle}
        placeholder="Title"
      />
      <TextInput
        style={styles.textInput}
        value={formText}
        multiline
        onChangeText={setFormText}
        placeholder="Journal Text"
      />
      <Button title="Save Changes" onPress={handleSave} />
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    padding: "5%",
  },
  input: {
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
});
