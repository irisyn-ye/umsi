import React, { useState } from 'react';
import { View, Text, StyleSheet, Button, Modal, Pressable } from 'react-native';
import { useDispatch, useSelector } from 'react-redux';
import { deleteJournalEntry } from '../features/journalSlice';
import { useNavigation } from '@react-navigation/native';

export default function JournalDetails({ route }) {
    const { entryId, title, text, promptId, promptText } = route.params;
    const dispatch = useDispatch();
    const navigation = useNavigation();
    const [alertVisible, setAlertVisible] = useState(false)

    const handleDelete = () => {
        dispatch(deleteJournalEntry(entryId));
        navigation.goBack();
    };

    const handleEdit = () => {
        // Assuming you have an 'EditJournalEntry' screen for editing
        navigation.navigate("Edit Journal", { entryId, title, text, promptId, promptText });
    };

    return (
        <View style={styles.container}>
            <Modal
                animationType="slide"
                transparent={true}
                visible={alertVisible}
                onRequestClose={() => {
                    setAlertVisible(!alertVisible);
                }}>
                <View style={styles.centeredView}>
                    <View style={styles.modalView}>
                        <Text>Are you sure you want to delete this entry?</Text>
                        <View style={[styles.buttonContainer, { justifyContent: 'space-around', width: "100%", paddingTop: "5%"} ]}>
                            <Button
                                title="CANCEL"
                                onPress={() => setAlertVisible(!alertVisible)} />

                            <Button
                                title="DELETE"
                                color="#ff2b2b"
                                onPress={() => {
                                    handleDelete()
                                    setAlertVisible(!alertVisible)
                                    navigation.navigate("Journals")
                                }} />
                        </View>
                    </View>
                </View>
            </Modal>
            <Text style={{ fontSize: 18, fontWeight: "bold", marginTop: 5, marginBottom: 5 }}>{title}</Text>
            <Text style={{ color: "#828282", marginBottom: 20 }}>Prompt: {promptText}</Text>
            <Text>{text}</Text>

            <View style={styles.buttonContainer}>
                <Button
                    title="Delete"
                    color="#ff2b2b"
                    onPress={() => setAlertVisible(true)} />
                <Button
                    title="Edit"
                    onPress={handleEdit} />
            </View>
        </View>
    );
};

const styles = StyleSheet.create({
    container: {
        flex: 1,
        padding: "5%",
    },
    buttonContainer: {
        flexDirection: "row",
        justifyContent: "space-around",
        marginTop: "auto",
    },
    centeredView: {
        flex: 1,
        justifyContent: 'center',
        alignItems: 'center',
        marginTop: 22,
    },
    modalView: {
        margin: 20,
        backgroundColor: 'white',
        borderRadius: 20,
        padding: 35,
        alignItems: 'center',
        shadowColor: '#000',
        shadowOffset: {
            width: 0,
            height: 2,
        },
    }
})
