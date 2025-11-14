// https://leetcode.com/problems/increment-submatrices-by-one/

impl Solution {
    pub fn range_add_queries(mut n: i32, queries: Vec<Vec<i32>>) -> Vec<Vec<i32>> {
        let mut mat: Vec<Vec<i32>> = vec![vec![0; (n + 1) as usize]; (n + 1) as usize];

        for query in queries {
            let [r1, c1, r2, c2] = query.try_into().unwrap();

            mat[r1 as usize][c1 as usize] += 1;
            mat[(r2 + 1) as usize][c1 as usize] -= 1;
            mat[r1 as usize][(c2 + 1) as usize] -= 1;
            mat[(r2 + 1) as usize][(c2 + 1) as usize] += 1;
        }

        for row in 1..=n {
            for col in 0..=n {
                mat[row as usize][col as usize] += mat[(row - 1) as usize][col as usize];
            }
        }

        for row in 0..=n {
            for col in 1..=n {
                mat[row as usize][col as usize] += mat[row as usize][(col - 1) as usize];
            }
        }

        let sub_mat: Vec<Vec<i32>> = mat[..n as usize]
            .iter()
            .map(|row| row[..n as usize].to_vec())
            .collect();
        
        sub_mat
    }
}
