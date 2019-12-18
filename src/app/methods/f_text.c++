#include <iostream>
using namespace std;

char* reallocAndVerify(char* str, int size)
{
    char *str_final = (char*) realloc(str,size);
    if (str_final == NULL)
    {
        cout << "ERROR" << endl;
        exit(1);
    }
    else 
    {
        return (str_final);
    }
}

char* str_patters(char *str)
{
    // the final str for python
    char* str_final = (char*) malloc(sizeof(char));
    
    // has 2 indices for the str received and str for return
    for (int i_str = 0, i_final = 0; str[i_str] != '\0'; i_str++, i_final++)
    {
        // swap the character for python interpreter 
        switch (str[i_str])
        {
            case '{':
                str_final[i_final] = '(';
                break;

            case '}':
                str_final[i_final] = ')';
                break;

            case '[':
                str_final[i_final] = '[';
                break;

            case ']':
                str_final[i_final] = ']';
                break;
            case '^':
                
        }

        // tolower the character
        if (str[i_str] >= 'A' && str[i] <= 'Z')
        {
            str[i_final] += 'a' + ('a' - 'A');
        }
    }
    return str_final;
}

int main(int argc, char *argv[])
{
    char str[] = "{sin[cos[x]]^25}";
    cout << str << str_patters(str) << endl;
    return 0;
}