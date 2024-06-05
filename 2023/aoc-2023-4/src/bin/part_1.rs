fn main() {
    let input = include_str!("./input_1.txt");

    println!("{}",part1(input))
}

fn part1(input: &str) -> u32 {
    let result: u32 = input.lines().map(|line|{
        let card: Card = parse_card(line.to_string());
        //println!("{:?}", &card);
        return evaluate_game(&card.win_nrs, card.test_nrs);
    }).sum();

    return result
}

#[derive(Debug,PartialEq)]
struct Card{
    id: u32,
    win_nrs: String,
    test_nrs: Vec<String>,
}

fn parse_card(card: String) -> Card{

    let subcard = card.replace("Card ", "");
    let split_card : Vec<String> = subcard.split(": ").map(|s| s.to_string()).collect();
    let id: u32 = split_card[0].replace(" ","").parse::<u32>().expect("Expect card id");
    let split_nums: Vec<String> = split_card[1].split(" | ").map(|s| s.to_string()).collect(); 
    let binding = split_nums[1].replace("  ", " ");
    let mut test_nrs: Vec<String> = binding.split(" ").map(|s| s.to_string()).collect();
    let win_nrs: String = split_nums[0].to_string();
    if test_nrs[0] == "" {
        test_nrs.remove(0);
    }



    return Card{
    id,
    win_nrs,
    test_nrs,
    };
}

fn evaluate_game(win_nrs: &str, test_nrs: Vec<String>) -> u32 {
    let mut result: u32= 0;
    let mut found_numbers: Vec<String> = Vec::<String>::new();

    let owned_win_nrs: String = " ".to_owned() + win_nrs + " ";
    for test_nr in test_nrs {
        let owned_test_nr: String = " ".to_owned() + &test_nr + " ";
        if owned_win_nrs.contains(&owned_test_nr) && !(found_numbers.contains(&test_nr)) {

            found_numbers.push(test_nr);
            if result == 0{
                result += 1;
            } else {
                result *= 2;
            }
        }
    }

    return result;
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_evaluation() {
        let r1: u32 = evaluate_game("41 48 83 86 17", ["83", "86", "6", "31", "17",  "9", "48", "53"].into_iter().map(|s| s.to_string()).collect());
        let r2: u32 = evaluate_game("13 32 20 16 61", ["61", "30", "68", "82", "17",  "32", "24", "19"].into_iter().map(|s| s.to_string()).collect());
        assert_eq!(r1, 8);
        assert_eq!(r2, 2);
    }
    #[test]
    fn test_parse_card() {
        let test_result: Card = Card{
            id: 1,
            win_nrs: "41 48 83 86 17".to_string(),
            test_nrs: ["83", "86", "6", "31", "17",  "9", "48", "53"].to_vec().into_iter().map(|s| s.to_string()).collect(),
        };
        let test_card = parse_card("Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53".to_string());
        assert_eq!(test_result, test_card);
    }
    #[test]
    fn test_part_1() {
        let input = include_str!("./test.text");
        let test_result = part1(input);
        assert_eq!(test_result, 13);
    }
    #[test]
    fn test_part_12() {
        let input = include_str!("./test_12.txt");
        let test_result = part1(input);
        assert_eq!(test_result, 512+512+1);
    }
    #[test]
    fn test_part_13_missing_first_number() {
        let input = include_str!("./test_13.txt");
        let test_result = part1(input);
        assert_eq!(test_result, 512+32);
    }
}
