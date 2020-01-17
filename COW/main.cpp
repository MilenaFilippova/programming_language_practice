#include <iostream>
#include <locale.h>
#include <cctype>
#include <string>
#include <fstream>


using namespace std;
string get_all_word(istream &is) ;
int cycle(int x, int y);
int cycle_two(int y);

int main()
{
	
	ifstream in("D:\\cow.txt");


	string str;	//считываемая строка из файла
	int temp=0;	

	if (!in.is_open())
	{ 
		cout<< "Unable to open text file . "<<endl; 
		return 1; 
	}  
	cout<<"File open"<<endl;
	
	int *buffer=new int[3000];
	int pos=0, k=0, l=0;
	int flag=0;
	while (!in.eof()) 
	{
			str = get_all_word(in);

			// значение текущей ячейки увеличить на 1
			if( str == "MoO")
			{
				temp++;
				buffer[pos]=temp;
				cout<<"MоO++="<<buffer[pos]<<endl;
			}
			//значение ​текущей ячейки уменьшить на 1
			else if(str == "MOo")
			{
				temp--;
				buffer[pos]=temp;
				cout<<"MOo-- ="<<buffer[pos]<<endl;
			}
			//// ввод значения в текущую ячейку
			else if(str == "oom")
			{
				int x;
				cout<<"Please enter number:"<<endl;
				cin>>x;
				buffer[pos]=x;
			}
			//OOM - вывод значения текущей ячейки
			else if(str == "OOM")
			{
				cout<<"buffer[pos]="<<buffer[pos]<<endl;
			}
			//moO - следующая ячейка
			else if(str == "moO")
			{
				pos++;
				cout<<"sdvig-- ="<<pos<<endl;
			}
			//mOo - предыдущая ячейка
			else if(str == "mOo")
			{
				pos--;
				cout<<"sdvig-- ="<<pos<<endl;
			}
			// обнулить значение в ячейке
			else if(str == "OOO")
			{
				buffer[pos]=0;
				cout<<"sdvig-- ="<<pos<<endl;
			}
		
			//Moo - если значение в ячейке равно 0, 
			//то ввести с клавиатуры, если значение не 0, то вывести на экран
			else if(str == "Moo")
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
			else if(str == "moo") 
			{
				k=buffer[pos];
				flag++;
			}
			else if( str == "MOO" )
			{
				l=buffer[pos];
				if(flag==1)
				{
					pos=cycle(k, l);
					flag=0;
				}
				else
				{
					pos=cycle_two(l);
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

int cycle(int x, int y)
{
	int i=0;
	for(i=x;i<y;i++){}

	return i;
}
int cycle_two(int y)
{
	int i=0;
	while(y)
	{
		i++;
		y--;
	}

	return i;
}
