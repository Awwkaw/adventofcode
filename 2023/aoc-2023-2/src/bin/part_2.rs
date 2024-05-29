
fn main() {
    let input = include_str!("./input_1.txt");

    println!("{}",part2(input))
}

pub fn part2(input: &str) -> u32{
    let result:u32 = input.lines().map(|line|{
        let subline = line.replace("Game ","");
        let split_line: Vec<String> = subline.split(": ").map(|s| s.to_string()).collect();
        
        game_power(&split_line[1]) 
    }).sum();

    return result
}

pub fn add(left: usize, right: usize) -> usize {
    left + right
}

pub fn game_power(game: &str) -> u32 {
    let mut game_mins: [u32;3] = [0, 0, 0];
    let game_mod = game.replace(";",",");

    for game_min in game_mod.split(", ").map(|subtest| 
                                {
                                    let mut local_min: [u32;3] = [0, 0, 0];
                                    let mut index: usize = 0;
                                    if subtest.contains("red"){
                                       index = 0; 
                                    }else if subtest.contains("green"){
                                       index = 1; 
                                    }else if subtest.contains("blue"){
                                       index = 2; 
                                    }
                                    let pieces: Vec<String> = subtest.split(' ').map(|s| s.to_string()).collect();
                                    let tnum: u32 = pieces[0].parse::<u32>().expect("Expected a number"); 
                                    if tnum > local_min[index] {
                                        local_min[index] = tnum;
                                    }
                                    return local_min
                                }) {
        if !(game_mins[0] >= game_min[0]) {
            game_mins[0] = game_min[0]
        }
        if !(game_mins[1] >= game_min[1]) {
            game_mins[1] = game_min[1]
        }
        if !(game_mins[2] >= game_min[2]) {
            game_mins[2] = game_min[2]
        }
    }
    return game_mins[0] * game_mins[1] * game_mins[2]
} 

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_single_game() {
        let result = game_power("1 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red");
        assert_eq!(result, 1560);
    }
    #[test]
    fn test_scenario() {
        let result = part2(include_str!("./test_1.txt"));
        assert_eq!(result, 2286);
    }
}

