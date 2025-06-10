#include <iostream>
#include <cstring>

using namespace std;

int vowelCount = 0;
int consonantCount = 0;
int keywordCount = 0;
int identifierCount = 0;
int digitCount = 0;
bool validMailID = false;

int yylex(char* input, int type);

int main() {
    cout << "Choose an input type:\n";
    cout << "1. Sentence\n";
    cout << "2. Code\n";
    cout << "3. Email\n";

    int choice;
    cin >> choice;

    switch (choice) {
        case 1: {
            char input[100];
            cin.ignore(); // Ignore newline character left in buffer
            cin.getline(input, sizeof(input));
            yylex(input, 1);
            break;
        }
        case 2: {
            char input[1000];
            cin.ignore(); 
            cin.getline(input, sizeof(input));
            yylex(input, 2);
            break;
        }
        case 3: {
            char input[100];
            cin.ignore(); 
            cin.getline(input, sizeof(input));
            yylex(input, 3);
            break;
        }
        default:
            cout << "Invalid choice";
    }

    return 0;
}

int yylex(char* input, int type) {
    char* token = nullptr;
    bool atSymbolFound = false;
    int dotCount = 0;

    switch (type) {
        case 1: // Sentence
            for (int i = 0; i < strlen(input); ++i) {
                char ch = tolower(input[i]);
                if (isalpha(ch)) {
                    if (ch == 'a' || ch == 'e' || ch == 'i' || ch == 'o' || ch == 'u') {
                        vowelCount++;
                    } else {
                        consonantCount++;
                    }
                }
            }
            cout << "Number of vowels: " << vowelCount << endl;
            cout << "Number of consonants: " << consonantCount << endl;
            break;
        case 2: // Code
            token = strtok(input, " \n\t");
            while (token != NULL) {
                if (strcmp(token, "int") == 0 || strcmp(token, "float") == 0 || strcmp(token, "return") == 0) {
                    keywordCount++;
                } else if (isalpha(token[0]) || token[0] == '_') {
                    identifierCount++;
                } else if (isdigit(token[0])) {
                    digitCount++;
                }
                token = strtok(NULL, " \n\t");
            }
            cout << "Number of keywords: " << keywordCount << endl;
            cout << "Number of identifiers: " << identifierCount << endl;
            cout << "Number of digits: " << digitCount << endl;
            break;
        case 3: // Email
            for (int i = 0; i < strlen(input); ++i) {
                if (input[i] == '@') {
                    atSymbolFound = true;
                } 
                if ((atSymbolFound = true) && input[i] == '.') {
                    dotCount++;
                }
            }
            validMailID = atSymbolFound && dotCount > 0;
            cout << "Is " << input << " a valid mail ID? " << (validMailID ? "Yes" : "No") << endl;
            break;
        default:
            cout << "Invalid input type";
    }

    return 0;
}
