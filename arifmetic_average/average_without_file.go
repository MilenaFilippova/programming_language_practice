package main

import (
	"fmt"
	"log"
	"strconv"
	"math"
	"strings"
)

func main() {
	var str = strings.Split("600 470 170 430 300"," ")
	var average float64 = 0
	var error=""  //проверка ввода
	var dispers float64= 0
	var numbers []int
	var numbers2 []int32

	//Для считывания данных определяется срез из 64 байтов.
	// В бесконечном цикле содержимое файла считывается в срез, а когда будет достигнут конец файла, 
	//то есть мы получим ошибку io.EOF, то произойдет выход из цикла.
	
	for i:=0; i<len(str); i++ {
		//	fmt.Print("str[i]",string(str[i]),"\n")
		//перевдим байт в число
		temp, err:=strconv.ParseInt(string(str[i]), 10, 64)
		if err != nil {
			log.Fatal(err)
		}
      
		fmt.Print("temp=",temp,"\n")
		numbers = append(numbers,int(temp))
		fmt.Print("numbers=",numbers,"\n")
		temp=0;
	}
	for i:=0; i<len(numbers); i++ {
		average += float64(numbers[i])
	}
	fmt.Print("average=",average,"\n")
	average /= float64(len(numbers))
	for i:=0; i<len(numbers); i++ {
		numbers2 = append(numbers2, int32(numbers[i]) - int32(average))
		dispers += float64( numbers2[i] * numbers2[i] ) 
	}
	//Когда мы имеем дело с генеральной совокупностью при вычислении дисперсии, мы делим на N (как и было сделано в рассмотренном нами примере).
	//Когда мы имеем дело с выборкой, при вычислении дисперсии делим на N-1.
	//будем считать что числа в файле - уже выборка
	dispers /= float64( len(numbers)-1 )
	var result = float64(math.Sqrt(float64(dispers)))
	if error==""{
		fmt.Println("Result:", result)
	}else{
		fmt.Println("error=",error)
	}
	
}
