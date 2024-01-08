class Solution {
public:
    bool isValid(std::string s) {
        std::stack<char> charStack;

        for (char c : s) {
            if (c == '(' || c == '{' || c == '[') {
                charStack.push(c);
            } else if (c == ')' || c == '}' || c == ']') {
                if (charStack.empty()) {
                    return false;
                }

                char top = charStack.top();
                charStack.pop();

                if ((c == ')' && top != '(') ||
                    (c == '}' && top != '{') ||
                    (c == ']' && top != '[')) {
                    return false;
                }
            }
        }

        return charStack.empty();
    }
};
