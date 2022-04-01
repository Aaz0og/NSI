// make a visual sorting algorithm
int main()
{
    int n;
    cout << "Enter the number of elements: ";
    cin >> n;
    int a[n];
    cout << "Enter the elements: ";
    for (int i = 0; i < n; i++)
        cin >> a[i];
    cout << "The elements in the array are: ";
    for (int i = 0; i < n; i++)
        cout << a[i] << " ";
    cout << endl;
    int temp;
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < n - 1; j++)
        {
            if (a[j] > a[j + 1])
            {
                temp = a[j];
                a[j] = a[j + 1];
                a[j + 1] = temp;
            }
        }
    }
    cout << "The elements in the sorted array are: ";
    for (int i = 0; i < n; i++)
        cout << a[i] << " ";
    cout << endl;
    return 0;
}
