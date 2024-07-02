use std::cmp::Ordering;

fn main() {
    let input = include_str!("input_1.txt");
    println!("{}",part2(input));
}

fn part2(input: &str) -> u64 {
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

    let mut val: u64 = joker_hand_type(&hand) * u64::pow(10,10);
    let cards: Vec<char> = hand.cards.chars().collect();
    for (i,card) in cards.into_iter().enumerate() {
        val += card_value(card) * u64::pow(10, 8-2*( i as u32));
    }

    return val;
}

fn joker_hand_type (hand: &Hand) -> u64 {
    let mut max_type: u64 = 0;
    let test_letters: [&str; 12] = ["A","K","Q","T","9","8","7","6","5","4","3","2"];
    if hand.cards.contains("J") {
        for letter in test_letters{
            let mut card_test = hand.cards.clone(); 
            card_test = card_test.replace("J",letter);
            max_type = u64::max(max_type,hand_type(&card_test));
        }
        return max_type;

    } else {
        return hand_type(&hand.cards);
    }
}

fn hand_type(cards: &str) -> u64{
        
    let types = card_types(&cards);
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

fn card_types(cards: &str) -> Vec<(char, u32)> {
    let mut types: Vec<(char, u32)> = Vec::new();
    let mut found: bool = false;
    for card in cards.chars() {
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
        return 01;
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
        let value: u64 = 61414010110;
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
        let res: Vec<Hand> = [
            Hand{cards:"32T3K".to_string(),bet:765,value:20302100313},
            Hand{cards:"T55J5".to_string(),bet:684,value:61005050105},
            Hand{cards:"KK677".to_string(),bet:28, value:31313060707},
            Hand{cards:"KTJJT".to_string(),bet:220,value:61310010110},
            Hand{cards:"QQQJA".to_string(),bet:483,value:61212120114}
        ].to_vec();
        for i in 0..5 {
            assert_eq!(res[i],parsed[i])
        }
    }
    #[test]
    fn test_part_2() {
        let input= include_str!("test_1.txt");
        let tres: u64 = part2(input);
        let res: u64 = 5905;
        assert_eq!(tres,res);
    }
}
