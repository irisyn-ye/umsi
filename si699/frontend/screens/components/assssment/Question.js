import { View, Text, Button, TouchableOpacity } from 'react-native';

const Question = ({ question, selectedOption, onAnswerSelect }) => {
  return (
    <View>
      <Text style={{paddingVertical: 20, fontSize: 20, textAlign: 'center'}}>{question.question}</Text>
      {question.options.map((option, index) => (
        <TouchableOpacity
          key={index}
          onPress={() => onAnswerSelect(option)}
          style={{
            padding: 10,
            backgroundColor: selectedOption === option ? 'lightblue' : 'lightgray',
            marginVertical: 5,
            borderWidth: selectedOption === option ? 2 : 0,
            borderColor: selectedOption === option ? 'blue' : 'transparent',
          }}
        >
          <Text>{option}</Text>
        </TouchableOpacity>
      ))}
    </View>
  );
};

export default Question;
