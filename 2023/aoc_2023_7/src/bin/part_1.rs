use std::cmp::Ordering;

fn main() {
    let input = include_str!("input_1.txt");
    println!("{}",part1(input));
}

fn part1(input: &str) -> u64 {
    let mut hands: Vec<Hand> = parse(input);
    let mut score: u64 = 0;
    hands.sort();
    for (i, hand) in hands.iter().enumerate() {
        score += (i as u64 + 1) * hand.bet;
    }
    return score;
}

#[derive(Clone,Debug)]
struct Hand {
    cards: String,
    bet: u64,
    value: u64,
}

impl Ord for Hand {
    fn cmp(&self, other: &Self) -> Ordering{
        (&self.value).cmp(&(other.value))
    } 
}

impl PartialOrd for Hand {
    fn partial_cmp(&self, other: &Self) -> Option<std::cmp::Ordering> {
        Some(self.value.cmp(&other.value))
    }
}

impl PartialEq for Hand {
    fn eq (&self, other: &Self) -> bool{
        (self.value == other.value) && (self.bet == other.bet)
    }
}

impl Eq for Hand {}

fn hand_value(hand: &Hand) -> u64 {

    let mut val: u64 = hand_type(&hand) * u64::pow(10,10);
    let cards: Vec<char> = hand.cards.chars().collect();
    for (i,card) in cards.into_iter().enumerate() {
        val += card_value(card) * u64::pow(10, 8-2*( i as u32));
    }

    return val;
}
fn hand_type(hand: &Hand) -> u64{
    let types = card_types(hand);
    if types[0].1 == 5 {
        return 7;
    } else if types[0].1 == 4 || types[1].1 == 4 {
        return 6;
    } else if (types[0].1 == 3 && types[1].1 == 2) || (types[0].1 == 2 && types[1].1 == 3) {
        return 5;
    } else if types[0].1 == 3 || types[1].1 == 3 || types[2].1 == 3 {
        return 4;
    } else if (types[0].1 == 2 && (types[1].1 == 2 || types[2].1 == 2)) || (types[1].1 == 2 && types[2].1 == 2) {
        return 3;
    } else if types[0].1 == 2 || types[1].1 == 2 || types[2].1 == 2 || types[3].1 == 2{
        return 2;
    } else {
        return 1;
    }
} 

fn card_types(hand: &Hand) -> Vec<(char, u32)> {
    let mut types: Vec<(char, u32)> = Vec::new();
    let mut found: bool = false;
    for card in hand.cards.chars() {
        for typ in &mut types {
            if typ.0 == card {
                typ.1 += 1; 
                found = true;
                break
            }
        }
        if !found {
           types.push((card, 1)); 
        }
        found = false;
    }
    return types;
    
}
fn card_value(card: char) -> u64 {
    if card == 'A'{
        return 14;
    } else if card == 'K' {
        return 13;
    } else if card == 'Q' {
        return 12;
    } else if card == 'J' {
        return 11;
    } else if card == 'T' {
        return 10;
    } else if card == '9' {
        return 9;
    } else if card == '8' {
        return 8;
    } else if card == '7' {
        return 7;
    } else if card == '6' {
        return 6;
    } else if card == '5' {
        return 5;
    } else if card == '4' {
        return 4;
    } else if card == '3' {
        return 3;
    } else {
        return 2;
    }
}

fn parse(input: &str) -> Vec<Hand>{
    let parsed: Vec<Hand> = input.lines().map(|x| {
        let parts: Vec<&str>= x.split(" ").collect();
        let cards = parts[0].to_string();
        let bet = parts[1].parse::<u64>().expect("Should be number");
        let mut hand: Hand=  Hand{
            cards,
            bet,
            value: 0,
        };
        hand.value = hand_value(&hand);
        return hand
    }).collect();
    return parsed;
}

#[cfg(test)]
mod tests{
    use super::*;

    #[test]
    fn test_create_hand() {
        let cards = "AAJJT";
        let bet = 1413;
        let value: u64 = 31414111110;
        let hand = Hand{
            cards: cards.to_string(),
            bet,
            value,
            };
        
        let test_value = hand_value(&hand);
        assert_eq!(hand.cards,cards);
        assert_eq!(hand.bet,bet);
        assert_eq!(hand.value,value);
        assert_eq!(test_value, value);
    }
    #[test]
    fn test_hand_comparison() {
        let input: String= "AAQQT 231\n22333 123".to_string();
        let parsed: Vec<Hand> = parse(&input);
        assert_eq!(parsed[1] > parsed[0], true);
    }
    #[test]
    fn test_parse_twoline() {
        let input: String= "AAQQT 231\n22333 123".to_string();
        let parsed: Vec<Hand> = parse(&input);
        let res: Vec<Hand> = [Hand{cards:"AAQQT".to_string(),bet:231,value:31414121210},Hand{cards:"22333".to_string(),bet:123,value:50202030303}].to_vec();
        assert_eq!(parsed,res);
    }
    #[test]
    fn test_parse_input() {
        let input= include_str!("test_1.txt");
        let parsed = parse(input);
    }
    #[test]
    fn test_part_1() {
        let input= include_str!("test_1.txt");
        let tres: u64 = part1(input);
        let res: u64 = 6440;
        assert_eq!(tres,res);
    }
}
