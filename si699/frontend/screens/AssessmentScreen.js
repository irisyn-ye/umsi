import React from 'react';
import { View, Text, StyleSheet, Button } from 'react-native';
import { useDispatch, useSelector } from 'react-redux';
import { getAssessment } from '../features/assessment/assessmentSlice';
import { useEffect } from 'react';

const AssessmentScreen = ({ navigation }) => {
    const assessmentInfo = useSelector(state => state.assessment);
    const noAssessmentData = Object.keys(assessmentInfo).length === 0
    const dispatch = useDispatch();

    useEffect(() => {
        dispatch(getAssessment());
    }, [dispatch]);

    return (
        <View style={styles.container}>
            <Text style={styles.title}>Assessment Results</Text>
            {!noAssessmentData && <View style={styles.resultsContainer}>
                {Object.keys(assessmentInfo).map((key, index) => (
                    <View key={index} style={styles.resultItem}>
                        <Text style={styles.bullet}>•</Text>
                        <View style={styles.resultTextContainer}>
                            <Text style={styles.resultKey}>{key}:</Text>
                            <Text style={styles.resultValue}>{assessmentInfo[key]}</Text>
                        </View>
                    </View>
                ))}
            </View>
            }
            <Button
                title="Start Assessment"
                onPress={() => {
                    navigation.navigate('Assessment Questions');
                }}
            />
        </View>
    );
};

const styles = StyleSheet.create({
    container: {
        flex: 1,
        justifyContent: 'center',
        alignItems: 'center',
        padding: 20,
    },
    title: {
        fontSize: 24,
        fontWeight: 'bold',
        marginBottom: 20,
    },
    resultsContainer: {
        borderWidth: 1,
        borderColor: '#ccc',
        borderRadius: 5,
        padding: 10,
        marginBottom: 20,
        width: '100%',
        maxHeight: 250,
        overflow: 'scroll',
    },
    resultItem: {
        flexDirection: 'row',
        marginBottom: 5,
    },
    bullet: {
        fontSize: 20,
        marginRight: 5,
    },
    resultTextContainer: {
        flexDirection: 'row',
        alignItems: 'center',
    },
    resultKey: {
        fontWeight: 'bold',
        marginRight: 5,
    },
    resultValue: {},
});

export default AssessmentScreen;
