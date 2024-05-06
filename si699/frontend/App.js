import { NavigationContainer } from '@react-navigation/native';
import { createStackNavigator } from '@react-navigation/stack';
import { createBottomTabNavigator } from '@react-navigation/bottom-tabs'

import LoginScreen from './screens/LoginScreen';
import NotesScreen from './screens/NotesScreen';
import SupportNetworkScreen from './screens/SupportNetworkScreen';
import AssessmentQuestions from './screens/AssessmentQuestions';
import Journals from './screens/Journals'
import NewEntry from './screens/components/journals/NewEntry';
import EditJournalEntry from './screens/components/journals/EditEntry';
import JournalPrompts from './screens/JournalPrompts';
import JournalDetails from './screens/JournalDetails';
import BlogScreen from './screens/components/BlogScreen'
import InitialAssessmentQuestions from './screens/InitialAssessmentQuestions';

import HomeScreen from "./screens/HomeScreen";
import ResourcesScreen from "./screens/ResourcesScreen";
import MapJourneyScreen from "./screens/AssessmentScreen";
import JourneyReviewScreen from "./screens/JourneyReviewScreen";
import 'react-native-gesture-handler';

import { configureStore } from '@reduxjs/toolkit'
import assessmentReducer from './features/assessment/assessmentSlice'
import journalReducer from './features/journalSlice';
import { Provider } from 'react-redux';
import { Button } from 'react-native';

export const store = configureStore({
  reducer: {
    assessment: assessmentReducer,
    journal: journalReducer,
  },
})

const Stack = createStackNavigator();
const HomeTab = createBottomTabNavigator();
const ResourcesStack = createStackNavigator();


const HomeStackScreen = () => {
  return (
    <HomeTab.Navigator
      screenOptions={({ route, navigation }) => ({
        tabBarVisible: ((route) => {
          const routeName = navigation.getState().routes[navigation.getState().index].name;
          // List all routes where you want to hide the tab bar
          const hideTabBarRoutes = ['Assessment'];
          return !hideTabBarRoutes.includes(routeName);
        })(route),
      })}
    >
      <HomeTab.Screen name="Home" component={HomeScreen} />
      <HomeTab.Screen name="Resources" component={ResourcesScreen} />
      <HomeTab.Screen name="Assessment" component={MapJourneyScreen} />
      <HomeTab.Screen name="Journey Overview" component={JourneyReviewScreen} />
    </HomeTab.Navigator>
  );
}

export default function App() {
  return (
    <Provider store={store}>
      <NavigationContainer>
        <Stack.Navigator initialRouteName='Login'>
          <Stack.Screen name="Login" component={LoginScreen} />
          <Stack.Screen name="HomeStack" component={HomeStackScreen} options={{ headerShown: false }} />
          <Stack.Screen name="Notes" component={NotesScreen} />
          <Stack.Screen name="SupportNetwork" component={SupportNetworkScreen} />
          <Stack.Screen name="Resources" component={ResourcesScreen} options={{ headerBackVisible: false }} />
          <Stack.Screen name="BlogScreen" component={BlogScreen}
            options={({ navigation }) => ({
              headerBackVisible: false, headerLeft: () => (
                <Button
                  onPress={() => navigation.navigate('HomeStack')}
                  title="<Back"
                />
              )
            })}
          />
          <Stack.Screen name="Assessment Questions" component={AssessmentQuestions} />
          <Stack.Screen name="Journals" component={Journals} />
          <Stack.Screen name="New Entry" component={NewEntry} />
          <Stack.Screen name="Journal Prompts" component={JournalPrompts} />
          <Stack.Screen name="Journal Details" component={JournalDetails} />
          <Stack.Screen name="Edit Journal" component={EditJournalEntry} />
          <Stack.Screen name="Assessment" component={InitialAssessmentQuestions} />
        </Stack.Navigator>
      </NavigationContainer>
    </Provider>
  )
}