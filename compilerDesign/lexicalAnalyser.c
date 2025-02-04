#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

#define MAX_TOKENS 1000
#define MAX_TOKEN_LENGTH 100

const char *keywords[] = {
    "auto", "break", "case", "char", "const", "continue", "default", "do", "double",
    "else", "enum", "extern", "float", "for", "goto", "if", "int", "long", "register",
    "return", "short", "signed", "sizeof", "static", "struct", "switch", "typedef",
    "union", "unsigned", "void", "volatile", "while"
};

char tokens[MAX_TOKENS][MAX_TOKEN_LENGTH];
char tokenTypes[MAX_TOKENS][MAX_TOKEN_LENGTH];
int tokenCount = 0;

int isKeyword(char *str) {
    for (int i = 0; i < sizeof(keywords) / sizeof(keywords[0]); i++) {
        if (strcmp(str, keywords[i]) == 0) {
            return 1;
        }
    }
    return 0;
}

void addToTokenTable(char *token, char *type) {
    if (tokenCount < MAX_TOKENS) {
        strcpy(tokens[tokenCount], token);
        strcpy(tokenTypes[tokenCount], type);
        tokenCount++;
    }
}

void scan(FILE *input) {
    char ch;
    char token[MAX_TOKEN_LENGTH];
    int j;
    int isPreprocessor = 0;

    while ((ch = fgetc(input)) != EOF) {
        if (isspace(ch)) continue;
        if (ch == '/') {
            char next = fgetc(input);
            if (next == '/') {
                while ((ch = fgetc(input)) != EOF && ch != '\n');
            } else if (next == '*') {
                char prev = 0;
                while ((ch = fgetc(input)) != EOF) {
                    if (prev == '*' && ch == '/') break;
                    prev = ch;
                }
            } else {
                ungetc(next, input);
                addToTokenTable("/", "operator");
            }
            continue;
        }

        if (ch == '#') {
            j = 0;
            token[j++] = ch;
            while ((ch = fgetc(input)) != EOF && isalpha(ch)) {
                token[j++] = ch;
            }
            token[j] = '\0';
            ungetc(ch, input);
            addToTokenTable(token, "preprocessor");
            isPreprocessor = strcmp(token, "#include") == 0;
            continue;
        }

   

        if (isalpha(ch) || ch == '_') {
            j = 0;
            token[j++] = ch;
            while ((ch = fgetc(input)) != EOF && (isalnum(ch) || ch == '_')) {
                token[j++] = ch;
            }
            token[j] = '\0';
            ungetc(ch, input);
            if (isKeyword(token)) {
                addToTokenTable(token, "keyword");
            } else {
                addToTokenTable(token, "identifier");
            }
            continue;
        }

        if (isdigit(ch)) {
            j = 0;
            token[j++] = ch;
            int hasDot = 0;
            while ((ch = fgetc(input)) != EOF && (isdigit(ch) || (ch == '.' && !hasDot))) {
                if (ch == '.') hasDot = 1;
                token[j++] = ch;
            }
            token[j] = '\0';
            ungetc(ch, input);
            addToTokenTable(token, "numeric constant");
            continue;
        }

        if (ch == '"' || ch == '\'') {
            char quote = ch;
            j = 0;
            token[j++] = ch;
            while ((ch = fgetc(input)) != EOF && ch != quote) {
                token[j++] = ch;
            }
            token[j++] = quote;
            token[j] = '\0';
            addToTokenTable(token, "string constant");
            continue;
        }

        token[0] = ch;
        token[1] = '\0';
        addToTokenTable(token, "operator");
    }
}

int main() {
    FILE *input = fopen("input.c", "r");
    if (!input) {
        printf("Error opening file.\n");
        return 1;
    }
    scan(input);
    fclose(input);

    for (int i = 0; i < tokenCount; i++) {
        printf("(%s, %s)\n", tokens[i], tokenTypes[i]);
    }
    return 0;
}
