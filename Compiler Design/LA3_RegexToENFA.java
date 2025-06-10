import java.util.*;
public class LA3_RegexToENFA {
   public static void main(String[] args) {
       Scanner scanner = new Scanner(System.in);
       System.out.print("Enter a regular expression: ");
       String regex = scanner.nextLine();
       String postfix = infixToPostfix(regex);
       System.out.println("Postfix expression is: " + postfix);
       Map<Integer, Map<Character, Set<Integer>>> transitionTable = convertToENFA(postfix);
       printTransitionTable(transitionTable);
   }
   private static String infixToPostfix(String infix) {
       StringBuilder postfix = new StringBuilder();
       Stack<Character> stack = new Stack<>();
       for (char c : infix.toCharArray()) {
           if (Character.isLetterOrDigit(c)) {
               postfix.append(c);
           } else if (c == '(') {
               stack.push(c);
           } else if (c == ')') {
               while (!stack.isEmpty() && stack.peek() != '(') {
                   postfix.append(stack.pop());
               }
               stack.pop(); // Pop '('
           } else {
               while (!stack.isEmpty() && precedence(stack.peek()) >= precedence(c)) {
                   postfix.append(stack.pop());
               }
               stack.push(c);
           }
       }
       while (!stack.isEmpty()) {
           postfix.append(stack.pop());
       }
       return postfix.toString();
   }
   private static int precedence(char operator) {
       if (operator == '|') {
           return 1;
       } else if (operator == '.') {
           return 2;
       }
       return 0;
   }
   private static Map<Integer, Map<Character, Set<Integer>>> convertToENFA(String postfix) {
       int stateCounter = 0;
       Map<Integer, Map<Character, Set<Integer>>> transitionTable = new HashMap<>();
       Stack<Integer> stateStack = new Stack<>();
       for (char c : postfix.toCharArray()) {
           if (Character.isLetterOrDigit(c)) {
               int startState = stateCounter++;
               int acceptState = stateCounter++;
               addTransition(transitionTable, startState, c, acceptState);
               stateStack.push(startState);
               stateStack.push(acceptState);
           } else if (c == '|') {
               int acceptState2 = stateStack.pop();
               int startState2 = stateStack.pop();
               int acceptState1 = stateStack.pop();
               int startState1 = stateStack.pop();
               int newStartState = stateCounter++;
               int newAcceptState = stateCounter++;
               addTransition(transitionTable, newStartState, 'ε', startState1);
               addTransition(transitionTable, newStartState, 'ε', startState2);
               addTransition(transitionTable, acceptState1, 'ε', newAcceptState);
               addTransition(transitionTable, acceptState2, 'ε', newAcceptState);
               stateStack.push(newStartState);
               stateStack.push(newAcceptState);
           } else if (c == '.') {
               int acceptState2 = stateStack.pop();
               int startState2 = stateStack.pop();
               int acceptState1 = stateStack.pop();
               int startState1 = stateStack.pop();
               addTransition(transitionTable, acceptState1, 'ε', startState2);
               stateStack.push(startState1);
               stateStack.push(acceptState2);
           }
       }
       return transitionTable;
   }
   private static void addTransition(Map<Integer, Map<Character, Set<Integer>>> transitionTable, int from, char input, int to) {
       transitionTable.computeIfAbsent(from, k -> new HashMap<>())
               .computeIfAbsent(input, k -> new HashSet<>())
               .add(to);
   }
   private static void printTransitionTable(Map<Integer, Map<Character, Set<Integer>>> transitionTable) {
       System.out.println("Transition Table:");
       System.out.println("___________________________________________");
       System.out.println("| from state	| input	| tostates");
       System.out.println("|-----------------------------------------|");
       for (Map.Entry<Integer, Map<Character, Set<Integer>>> entry : transitionTable.entrySet()) {
           int state = entry.getKey();
           Map<Character, Set<Integer>> transitions = entry.getValue();
           System.out.print("| " + state + "\t\t\t|");
           for (Map.Entry<Character, Set<Integer>> transition : transitions.entrySet()) {
               char input = transition.getKey();
               Set<Integer> toStates = transition.getValue();
               System.out.print(" " + input + "\t\t\t| " + toStates + "\t\t\t");
           }
           System.out.println();
       }
       System.out.println("___________________________________________");
   }
}
