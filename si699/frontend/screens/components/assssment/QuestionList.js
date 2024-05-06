import React, { useState } from 'react';
import { View, Button } from 'react-native';
import Question from './Question';
import { useSelector } from 'react-redux';

const QuestionList = ({ questions, currentQuestionIndex, onAnswerSelect, setCurrentQuestionIndex, selectedOption, navigation, skipUserType }) => {
  const [isAnswerSelected, setIsAnswerSelected] = useState(false);


  const handleNextQuestion = () => {
    setCurrentQuestionIndex(currentQuestionIndex + 1);
    setIsAnswerSelected(false);
  };

  const handlePreviousQuestion = () => {
    setCurrentQuestionIndex(currentQuestionIndex - 1);
    setIsAnswerSelected(false);
  };

  const handleAnswerSelect = (answer) => {
    onAnswerSelect(currentQuestionIndex, answer);
    setIsAnswerSelected(true);
  };

  const handleFinish = () => {
    navigation.navigate('Assessment');
  };

  return (
    <View>
      <Question
        question={questions[currentQuestionIndex]}
        onAnswerSelect={handleAnswerSelect}
        selectedOption={selectedOption}
      />
      <View style={{ flexDirection: 'row', justifyContent: 'space-between' }}>
        {currentQuestionIndex > 0 && !skipUserType && (
          <Button title="Previous" onPress={handlePreviousQuestion} />
        )}
        <View style={{ flex: 1 }} />
        {currentQuestionIndex < questions.length - 1 ? (
          <Button title="Next" onPress={handleNextQuestion} disabled={!isAnswerSelected} />
        ) : (
          <Button title="Finish" onPress={handleFinish} disabled={!isAnswerSelected} />
        )}
      </View>
    </View>
  );
};

export default QuestionList;
