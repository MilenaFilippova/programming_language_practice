package main
//import s "strings"
//import "fmt"  
import (
    "fmt" //реализует форматирование для входных и выходных данных.
    "os"  //ввод ч/з консоль
    "bufio"	//для ввода в консоль с пробелами 
    
)
func main ()  {

	var pr = fmt.Println

  var count_operat=0  //счетчики
	var count_numeric=0
	var сount_space =0
  
	var error=""  //проверка ввода
  //var formula="/ + 3 10 * + 2 3 - 3 5"

  
  reader := bufio.NewReader(os.Stdin)
   fmt.Print("You can translate a prefix expression into an infix expression. For example / + 3 10 * + 2 3 - 3 5  -> ((3+10)/((2+3)*(3-5)))) \n")
    fmt.Print("Enter text: ")
    formula, _ := reader.ReadString('\n')

	
  idx_spaces:=[]int{}
	var str=" "
	var temp1=""   // для временных значений

	if formula=="" {
		error="Вы ничего не ввели."
	} 
 
  for i:=len(formula)-2; i>=0; i-- {  //если с консоли задавали выражание
    //for i:=len(formula)-2; i>=0; i-- {  //если сами задали в программе
		if((formula[i]>=48 && formula[i]<=57) || (formula[i]>=65 && formula[i]<=90) || (formula[i]>=97 && formula[i]<=122))	{//если цифра или буква
      сount_space=0	//занулим счетчик пробелов
      temp1=string(formula[i])+ temp1
    } else if(formula[i]=='/' || formula[i]=='*' || formula[i]=='+' || formula[i]=='-') {
        
        сount_space=0	//занулим счетчик пробелов
        count_operat++
        idx_spaces=index_space(str) //находим индексы всех пробелов строке

        if(count_operat>=count_numeric) {
          str=mysplice(str,idx_spaces[0], 1, string(formula[i]) ) //для унарного минуса
          str=mysplice(str,idx_spaces[0], 0, "(" )
          str=mysplice(str,idx_spaces[1], 0, ")" )
				} else {
            str=mysplice(str,idx_spaces[0], 1, "(" )  //там где был первый пробел вставим (
            str=mysplice(str,idx_spaces[1], 1, string(formula[i]) )  //там где был второй пробел вставим знак
            str=mysplice(str,idx_spaces[2], 0, ")" ) //там где был третий пробел вставим ) и пробел останется
				}

		} else if(string(formula[i])==" ") {	
				сount_space++

				if(temp1!=""){
          str=string(temp1)+string(str)
					count_numeric++
					temp1=""  //очищаем временные значения
				}

				str=" "+string(str)
		} else {
				error="Некорректный  ввод. Лишние знаки"
				break
		}

		if(сount_space>1){
				error="Некорректный ввод. Проверьте количество пробелов."
				break
			}
      
  }
  if error==""{
			 pr("infics result=",str)
	}else{
      pr("error=",error)
  }
}

func index_space(str string) []int {
space:=" "  //пробел
idx_spaces:=[]int{}
for i, r := range str {

        if string(r) == space {
          idx_spaces=append( idx_spaces, i)
      }

    }
    return idx_spaces
}



func mysplice(str string, idx_spaces int,del int, symbol string,) string {
  temp_str:=""
  for index, value := range str{

    if index ==  idx_spaces{  //дошли до пробела
      temp_str=temp_str+symbol

      if del==0{ 
        break
      }

    }else{
      temp_str=temp_str+string(value)
    }
    
  }
  
  if del!=0{  //возвращаем строку в которой заменен один элемент
    return temp_str
  }else{
    //встаили эллемнт ,остальную строку дописываем 
    var next = idx_spaces+1

    for j := idx_spaces; j <= len(str)-1; j++ {

      temp_str=temp_str + string(str[j])
      next++
    }
  } 
  return temp_str
}