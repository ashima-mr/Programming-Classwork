#include <iostream>
#include <stack>
#include <string>
#include <algorithm>

using namespace std;

// Function to check if the given character is an operand (letter or digit)
bool isOperand(char c) {
    return isalpha(c) || isdigit(c);
}

// Function to get the precedence of the operator
int precedence(char op) {
    switch(op) {
        case '+':
        case '-':
            return 1;
        case '*':
        case '/':
            return 2;
        case '^':
            return 3;
        default:
            return 0;
    }
}

// Function to reverse a string
string reverseString(const string& str) {
    string reversed = str;
    reverse(reversed.begin(), reversed.end());
    return reversed;
}

// Function to convert infix expression to prefix expression
string infixToPrefix(string infix) {
    stack<char> stk;
    string postfix;

    // Reverse the infix expression
    infix = reverseString(infix);

    for (char& c : infix) {
        if (isOperand(c)) {
            postfix += c;
        } else if (c == ')') {
            stk.push(c);
        } else if (c == '(') {
            while (!stk.empty() && stk.top() != ')') {
                postfix += stk.top();
                stk.pop();
            }
            stk.pop(); // Pop ')'
        } else { // Operator
            while (!stk.empty() && precedence(stk.top()) >= precedence(c)) {
                postfix += stk.top();
                stk.pop();
            }
            stk.push(c);
        }
    }

    // Pop remaining operators from the stack
    while (!stk.empty()) {
        postfix += stk.top();
        stk.pop();
    }

    // Reverse the result to get the prefix expression
    return reverseString(postfix);
}

int main() {
	cout << "21BAI1830\n" << endl;
    string infix = "a+b*c-(d/e+f*g*h)";

    cout << "Infix expression: " << infix << endl;
    cout << "Prefix expression: " << infixToPrefix(infix) << endl;

    return 0;
}

