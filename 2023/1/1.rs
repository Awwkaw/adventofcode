use std::env;
use std::fs;
use std::collections::HashMap;

fn main() {
    let args: Vec<String> = env::args().collect();
    let file_path: &String = &args[1];

    let contents = fs::read_to_string(file_path)
        .expect("Should have been able to read to string");


    let nlines = linenum(&contents);
    let numbers: Vec<u32> = find_numbers(&contents);


    println!("Answer one: {}", numbers.iter().sum::<u32>());

    let numbers_p2: Vec<u32> = find_numbers_p2(&contents);
    println!("Answer two: {}", numbers_p2.iter().sum::<u32>());

    
}

fn find_numbers(text: &String) -> Vec<u32> {
    
    let mut result: Vec<u32> = Vec::new();
    let mut first = 'a';
    let mut last = 'a';

    let radix: u32 = 10;

    for letter in text.chars(){

        if (first == 'a') & letter.is_numeric() {
            first = letter;
            last = letter;
        }  else if letter.is_numeric(){
            last = letter;
        }
        if letter == '\n' {
            
            let l1 = first.to_digit(radix);
            let l2 = last.to_digit(radix);
            match (l1,l2){
                (Some(x), Some(y)) => result.push(10*x+y),
                _ => println!("Unsuccessfull")
            }
            first = 'a';
            last = 'a';
            continue;
        }
        
    }
    
    return result;
}

fn find_numbers_p2(text: &String) -> Vec<u32> {
    
    let mut result: Vec<u32> = Vec::new();
    let number_names: [&str; 9] = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"];
    let mut first = 'a';
    let mut last = 'a';
    let mut temp_string = String::new();
    let num_dict: HashMap <String,char> = number_spelling();

    let radix: u32 = 10;

    for letter in text.chars(){

        if (first == 'a') & letter.is_numeric() {
            first = letter;
            last = letter;
        }  else if letter.is_numeric(){
            last = letter;
        }
        temp_string.push(letter.clone());
        for number_name in number_names {
            if temp_string.contains(&number_name.to_string()) {
                let temp_num = match num_dict.get(number_name) {
                    Some(x) => x.clone(),
                    _ => 'n'.clone(),
                }; 
                if temp_num == 'n' {
                    println!("found bad number from string {temp_string}");
                }

                if (first == 'a') & temp_num.is_numeric() {
                    first = temp_num;
                    last = temp_num;
                }  else if temp_num.is_numeric(){
                    last = temp_num;
                }
                temp_string = temp_string.chars().last().unwrap().to_string();
                break

            }
        }

        if letter == '\n' {
            
            // println!("{first} and {last}");
            let l1 = first.to_digit(radix);
            let l2 = last.to_digit(radix);
            match (l1,l2){
                (Some(x), Some(y)) => result.push(10*x+y),
                _ => println!("Unsuccessfull")
            }
            first = 'a';
            last = 'a';
            temp_string = String::new();
            continue;
        }
        
    }
    
    return result;
}
fn linenum(text: &String) -> i32{
    let mut nlines = 0;

    for char in text.chars() {
        if char == '\n' {
            nlines += 1;
        }
    }

    return nlines;
}

fn number_spelling() -> HashMap<String,char> {
    let mut number_spelling = HashMap::new();
        number_spelling.insert(
            "one".to_string(), 
            '1', 
            );
        number_spelling.insert(
            "two".to_string(), 
            '2', 
            );
        number_spelling.insert(
            "three".to_string(), 
            '3',
            );
        number_spelling.insert(
            "four".to_string(), 
            '4',
            );
        number_spelling.insert(
            "five".to_string(), 
            '5',
            );
        number_spelling.insert(
            "six".to_string(), 
            '6',
            );
        number_spelling.insert(
            "seven".to_string(), 
            '7',
            );
        number_spelling.insert(
            "eight".to_string(), 
            '8',
            );
        number_spelling.insert(
            "nine".to_string(), 
            '9',
            );
        return number_spelling;
}
