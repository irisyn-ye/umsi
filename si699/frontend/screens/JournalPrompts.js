import { FlatList, Text, TouchableOpacity, StyleSheet, View } from 'react-native';
import { useNavigation } from '@react-navigation/native';
import promptList from './components/journals/promptArray';

const JournalPrompts = () => {
    const navigation = useNavigation();

    return (
        <View style={styles.container}>
            <FlatList
                data={promptList}
                key={(item) => item.promptId.toString()}
                renderItem={({ item }) => (
                    <TouchableOpacity
                        style={styles.button}
                        onPress={() => navigation.navigate('New Entry', { promptId: item.id })}>
                        <Text style={{fontSize: 16}}>{item.prompt}</Text>
                    </TouchableOpacity>

                )}
            />
        </View>

    );
};

const styles = StyleSheet.create({
    container: {
        flex: 1,
        padding: "5%",
    },
    button: {
        backgroundColor: 'lightblue',
        padding: 15,
        marginBottom: 10,
        borderRadius: 10,
    },
})

export default JournalPrompts;
