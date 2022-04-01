# include <iostream>
using namespace std;


int main() {
    char op;
    float num1,num2;
    cout << "Entrer une opération: +, -, *, /: ";
    cin >> op;
    cout << "Entrer deux nombres: ";
    cin >> num1 >> num2;
    switch (op)
    {
    case '+':
        cout << num1 << " + " << num2 << " = " << num1+num2;
        break;
    case '-':
        cout << num1 << " - " << num2 << " = " << num1-num2;
        break;
    case '*':
        cout << num1 << " x " << num2 << " = " << num1*num2;
        break;
    case '/':
        cout << num1 << " / " << num2 << " = " << num1/num2;
        break;
    default:
        // Si aucun des opérateurs si dessus n'est entré afficher un message d'erreur
        cout << "Erreur: opérateur non reconnu!";
        break;
    }

    return 0;
}