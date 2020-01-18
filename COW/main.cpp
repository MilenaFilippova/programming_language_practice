#include <iostream>
#include <locale.h>
#include <cctype>
#include <string>
#include <fstream>


using namespace std;
string get_all_word(istream &is) ;

int main()
{
	
	ifstream in("D:\\cow.txt");
	string *str = new string[3000]; //сто строк

	//string str;	//считываемая строка из файла
	int temp=0;	

	if (!in.is_open())
	{ 
		cout<< "Unable to open text file . "<<endl; 
		return 1; 
	}  
	cout<<"File open"<<endl;
	
	int *buffer=new int[3000];
	int pos=0, k=0, l=0;
	int brc = 0;
	int flag=0;
	int index=0;
	while (!in.eof()) 
	{
			str[index] = get_all_word(in);
			cout<<"str="<<str[index]<<endl;
			index++;
	}
	index=0;
	for (int i = 0; i < sizeof(str); ++i) 
	{
			// значение текущей ячейки увеличить на 1
			if( str[index] == "MoO")
			{
				temp++;
				buffer[pos]=temp;
				cout<<"MоO++="<<buffer[pos]<<endl;
			}
			//значение ​текущей ячейки уменьшить на 1
			else if(str[index] == "MOo")
			{
				temp--;
				buffer[pos]=temp;
				cout<<"MOo-- ="<<buffer[pos]<<endl;
			}
			//// ввод значения в текущую ячейку
			else if(str[index] == "oom")
			{
				int x;
				cout<<"Please enter number:"<<endl;
				cin>>x;
				buffer[pos]=x;
			}
			//OOM - вывод значения текущей ячейки
			else if(str[index] == "OOM")
			{
				cout<<"buffer[pos]="<<buffer[pos]<<endl;
			}
			//moO - следующая ячейка
			else if(str[index] == "moO")
			{
				pos++;
				cout<<"sdvig-- ="<<pos<<endl;
			}
			//mOo - предыдущая ячейка
			else if(str[index] == "mOo")
			{
				pos--;
				cout<<"sdvig-- ="<<pos<<endl;
			}
			// обнулить значение в ячейке
			else if(str[index] == "OOO")
			{
				buffer[pos]=0;
				cout<<"sdvig-- ="<<pos<<endl;
			}
		
			//Moo - если значение в ячейке равно 0, 
			//то ввести с клавиатуры, если значение не 0, то вывести на экран
			else if(str[index] == "Moo")
			{
				if( buffer[pos] == 0 )
				{
					int x;
					cout<<"Please enter number:"<<endl;
					cin>>x;
					buffer[pos]=x;
					cout<<"sdvig-- ="<<pos<<endl;
				}
				else
					cout<<"buffer[pos] ="<<buffer[pos]<<endl;
			}
			else if(str[index] == "moo") 
			{
				cout<<"go cicle1"<<endl;
				 if (!buffer[pos]) 
				 {
					brc++;
					while (brc) 
					{
						index ++;
						if (str[index] == "moo")
							++brc;
						if (str[index] == "MOO")
							--brc;
					}
					
				 } 
				 else
					continue;
			}
			else if (str[index] == "MOO") 
			{
				cout<<"go cicle"<<endl;
				if (!buffer[pos])
					continue;
				else 
				{
					cout<<"go cicle2"<<endl;
					if (str[index] == "MOO")
						brc++;
					while (brc) 
					{
						index--;
						if (str[index] == "moo")
							brc--;
						if (str[index] == "MOO")
							brc++;
					}
					index--;
				}
			}
			else
			{
				cout<<"undefined"<<endl;
			}


	}
				
    
	cout<<"Result = "<<buffer[pos]<<endl;
	in.close();
	system("pause");
	return 0;
}

string get_all_word(istream &is) 
{
    string w;
    is >> w;
    return w;
}

