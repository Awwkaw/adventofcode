
fn main() {
    let input = include_str!("./input_1.txt");

    println!("{}",part1(input))
}

pub fn part1(input: &str) -> i32{
    let limits: [u32; 3] = [12,13,14];
     
    let result:i32 = input.lines().map(|line|{
        let subline = line.replace("Game ","");
        let split_line: Vec<String> = subline.split(": ").map(|s| s.to_string()).collect();
        let idx = split_line[0].parse::<i32>().expect("Expect game number");
        
        legal_game(&split_line[1], idx, limits) 
    }).sum();

    return result
}

pub fn add(left: usize, right: usize) -> usize {
    left + right
}

pub fn legal_game(game: &str, idx: i32, limits: [u32; 3]) -> i32 {
    let mut possible: bool = true;

    let legal_hands = game.split("; ").map(|hand| {
        let mut possible: bool = true;
        for test in hand.split(", ").map(|subtest| 
                                        {
                                            let mut limit: u32 = 0;
                                            let mut res: bool = true;
                                            if subtest.contains("red"){
                                               limit = limits[0]; 
                                            }else if subtest.contains("green"){
                                               limit = limits[1]; 
                                            }else if subtest.contains("blue"){
                                               limit = limits[2];
                                            }
                                            let pieces: Vec<String> = subtest.split(' ').map(|s| s.to_string()).collect();
                                            let tnum: u32 = pieces[0].parse::<u32>().expect("Expected a number"); 

                                            if tnum > limit{
                                                res = false;
                                            }
                                            return res
                                        }) {
            if !test & possible{
                possible = false;
            }
        }
        return possible
    });
    for hand in legal_hands {
        if !hand{
        possible = false
        }
    }
    let mut result: i32 = 0;
    if possible {result = idx;}
    return result
} 

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn it_works() {
        let result = add(2, 2);
        assert_eq!(result, 4);
    }
    #[test]
    fn test_single_game() {
        let result = legal_game("1 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red", 4, [10,12,20]);
        assert_eq!(result, 0);
    }
    #[test]
    fn test_scenario() {
        let result = part1(include_str!("./test_1.txt"));
        assert_eq!(result, 8);
    }
}

