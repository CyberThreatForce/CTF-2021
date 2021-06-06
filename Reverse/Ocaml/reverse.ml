let strequal str1 str2 =
let rec chevalo lst string i =
match lst, string with
| e::q, e1::q1 -> e=e1 && chevalo q q1 (i+1)
| [], [] -> true
| [], _ -> false
| _, [] -> false in
chevalo str1 str2 0
;;

let rec listequal l1 l2=
match l1, l2 with
| e::q, e1::q1 when e=e1 -> true && listequal q q1
| [], [] -> true
| e::q, e1::q1 -> false
| _, _ -> false
;;

let xor data key=
let rec xor_tmp tab1 key i len =
match tab1, i with
| [], _ -> []
| e::q, i when i=len -> (Int.logxor (List.nth key i) e)::xor_tmp q key 0 len
| e::q, i -> (Int.logxor (List.nth key i) e )::xor_tmp q key (i+1) len in
xor_tmp data key 0 ((List.length key) -1)
;;

let rec char2int = function
| e::q -> (int_of_char e ):: char2int q
| [] -> []
;;


let string2char str =
let rec string2char_tmp str size i=
match i with
| i when i=size -> []
| i -> str.[i]:: string2char_tmp str size (i+1) in
string2char_tmp str (String.length str) 0
;;
let rec firstCheck flag magie =
match flag, magie with
| e::q, e1::q1 when e=e1 ->  firstCheck q q1
| [], e1::q1 -> false
| e::q,  [] -> true
| _, _ -> false
;;

let str = "CYBERTF{Not-S0Easy-Fake-Flag}";;
let key = [5; 122; 83; 213; 131; 216; 195; 254];;
let fst = [67; 89; 66; 69; 82; 84; 70; 123; 71; 111];;
let data = [105; 27; 61; 178; 220; 177; 176; 161; 65; 73; 19; 177; 220; 233; 173;
 161; 70; 46; 21; 138; 178; 239; 250; 203; 103; 78; 50; 237; 186; 239; 243; 198;
 54; 77; 98; 177; 178; 238; 250; 198; 55; 75; 106; 224; 181; 236; 241; 200; 54; 66;
 48; 177; 180; 239; 251; 205; 60; 67; 107; 228; 187; 224; 190];;



if (Array.length (Sys.argv)) != 2 then begin
  print_endline (Sys.argv.(0)^" FLAG");
  (* exit 1 *)
end
else begin
  if firstCheck (char2int(string2char Sys.argv.(1))) fst then begin
    let nextFlag = String.sub (Sys.argv.(1)) 10 (String.length (Sys.argv.(1)) -10) in
    print_endline nextFlag;
    if listequal (xor (char2int(string2char nextFlag)) key)  data then
      print_endline "Success"
    else begin
      print_endline "failed";
      exit 0
    end
    end
  else
    print_endline "failed"
end
;;
