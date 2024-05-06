import { View, Text, ScrollView, Image, StyleSheet, TextInput, Pressable, FlatList } from 'react-native';
const BlogBlock = ({ blog }) => (
    <View style={styles.blogBlock}>
        <Image source={blog.image} style={styles.image} />
        <Text style={styles.title}>{blog.title}</Text>
        <Text style={styles.author}>Author: {blog.author}</Text>
        <Text style={styles.summary}>{blog.summary}</Text>
        <View style={styles.tagGroup}>
            {blog.tags?.map((tag, i) => <Text key={i} style={styles.tag}>{tag}</Text>)}
        </View>
    </View>
);

export default BlogBlock;

const styles = StyleSheet.create({
    blogBlock: {
        borderWidth: 1,
        borderColor: '#ccc',
        marginBottom: 20,
        padding: 20,
        width: '80%',
        backgroundColor: '#f9f9f9',
    },
    image: {
        width: '100%',
        height: 200,
        marginBottom: 10,
    },
    title: {
        fontSize: 20,
        fontWeight: 'bold',
        marginBottom: 5,
    },
    author: {
        fontSize: 16,
        marginBottom: 5,
    },
    summary: {
        fontSize: 16,
    },
    tag: {
        backgroundColor: "lightblue",
        fontSize: 12,
        borderRadius: 12,
        height: 24,
        width: 'fit-content',
        paddingHorizontal: 10,
        paddingVertical: 4,
        textAlign: 'center',
        overflow: 'hidden'
    },
    tagGroup: {
        flexDirection: 'row',
        gap: 5,
        justifyContent: 'flex-end'
    }
});