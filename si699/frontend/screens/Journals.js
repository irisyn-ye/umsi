import React, { useEffect } from 'react';
import { View, Text, TouchableOpacity, FlatList } from "react-native";
import { useSelector, useDispatch } from 'react-redux';
import { useNavigation } from '@react-navigation/native';
import { fetchJournalEntries } from '../features/journalSlice';

export default function Journals() {
    const navigation = useNavigation();
    const journalList = useSelector(state => state.journal.entries);
    const dispatch = useDispatch();

    const formatDate = (timestamp) => {
        const date = new Date(timestamp);
        const month = date.getMonth() + 1; // getMonth() is zero-based
        const day = date.getDate();
        // Format the date as MM-DD. Adjust formatting as needed.
        return `${month < 10 ? `0${month}` : month}/${day < 10 ? `0${day}` : day}`;
    };

    useEffect(() => {
        dispatch(fetchJournalEntries());
    }, [dispatch]);

    return (
        <View style={{ flex: 1, justifyContent: 'flex-start', margin: "10%", }}>
            <TouchableOpacity
                style={{
                    backgroundColor: 'lightblue',
                    padding: 15,
                    marginBottom: 10,
                    borderRadius: 10,
                    alignItems: 'center'
                }}
                onPress={() => navigation.navigate('Journal Prompts')}
            >
                <Text style={{ fontSize: 18, fontWeight: "bold" }}>See the Prompt List</Text>
            </TouchableOpacity>

            <Text style={{ fontSize: 18, fontWeight: "bold", alignItems: 'center', textAlign:'center', marginTop:"10%", marginBottom: 5 }}>List of Journals</Text>
            <FlatList
                data={journalList}
                key={(item) => item.entryId.toString()}
                renderItem={({ item }) => (
                    <TouchableOpacity
                        style={{
                            marginBottom: "3%",
                            padding: "2%",
                            borderBottomWidth: 1,
                            borderColor: "#828282",
                            flex:1,
                            flexDirection: "row",
                            justifyContent: 'space-between'
                        }}
                        onPress={() => navigation.navigate('Journal Details', item)}>
                        <Text>{item.title}</Text>
                        <Text>
                            {formatDate(item.timestamp)} {'>'} 
                        </Text>
                    </TouchableOpacity>

                )}
            />
        </View>
    );
}
