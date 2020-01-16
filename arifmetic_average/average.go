package main

import (
	"fmt"
	"io"
	"os"
	"log"
	"strconv"
	"math"
	"bufio"
)

func main() {
	data := make( []byte, 64)
	numbers:=[]int{}
	numbers2 :=[]int32{}
	var average float64= 0
	var error=""  //проверка ввода

	reader := bufio.NewReader(os.Stdin)
    fmt.Print("Enter filename (for example: inp1.txt)  : ")
    filename, err := reader.ReadString('\n')
	if err != nil {
		fmt.Println(err)
		os.Exit(1)
	}
	if filename=="" {
		error="Вы ничего не ввели."
	}

	fmt.Println("Hello World")
	file, err := os.Open(string(filename))
	if err != nil {
		fmt.Println(err)
		os.Exit(1)
	}
	defer file.Close()
	//Для считывания данных определяется срез из 64 байтов.
	// В бесконечном цикле содержимое файла считывается в срез, а когда будет достигнут конец файла, 
	//то есть мы получим ошибку io.EOF, то произойдет выход из цикла.
	
	//var numbers = [600,470,170,430,300]
	var dispers float64= 0

	for {
			n, err := file.Read(data)
			if err == io.EOF { // если конец файла
				break // выходим из цикла
			}
			fmt.Print(string(data[:n]))
			//перевдим байт в число
			numbers[n], err=strconv.Atoi(string(data[:n]))
			if err != nil {
				log.Fatal(err)
			}
	}
	for i:=0; i<len(numbers); i++ {
		average += float64(numbers[i])
	}
	average /= float64(len(numbers))
	for i:=0; i<len(numbers); i++ {
		numbers2[i] = int32(numbers[i]) - int32(average)
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
