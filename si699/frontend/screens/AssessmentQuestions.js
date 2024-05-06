import React, { useState } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import { setAnswer } from '../features/assessment/assessmentSlice';
import QuestionList from './components/assssment/QuestionList';
import quizQuestions from './components/assssment/questionArray';
import { View } from 'react-native';


const AssessmentQuestions = ({ navigation }) => {
    const userType = useSelector(state => state.assessment[0])

    const [currentQuestionIndex, setCurrentQuestionIndex] = useState(userType ? 1 : 0);
    const [selectedOption, setSelectedOption] = useState({}); // Initialize selectedOption state
    const dispatch = useDispatch()

    const handleAnswerSelect = (questionIndex, answer) => {
        dispatch(setAnswer({ question: questionIndex, answer }));
        setSelectedOption(answer); // Update selectedOption state
    };

    return (
        <View>
            <QuestionList
                questions={quizQuestions}
                currentQuestionIndex={currentQuestionIndex}
                skipUserType={userType}
                onAnswerSelect={handleAnswerSelect}
                setCurrentQuestionIndex={setCurrentQuestionIndex}
                navigation={navigation}
                selectedOption={selectedOption} // Pass selectedOption state to QuestionList
            />
        </View>
    );
};

export default AssessmentQuestions;

