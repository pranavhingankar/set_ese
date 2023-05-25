#include <iostream>
#include <cstdio>

using namespace std;

int main()
{
    int count = 10;
    char str[10];
    FILE *fp=tmpfile();
    char *filename = "file.txt";
    fp = fopen(filename,"w+");
    fputs("An example file\n", fp);
    fputs("Filename is file.txt\n", fp);
    rewind(fp);
    while(feof(fp) == 0)
    {
        fgets(str,count,fp);
        cout << str << endl;
    }
    fclose(fp);
    return 0;
}