pragma solidity ^0.4.22;
contract AccountUnlock{
    string  password = 'JDUFHWUFHNYM34394';
    string private flag = "CYBERTF{S0lIdiTy_T0_Th3_M0oN_!}";
    function verify(string memory _password) public view returns (string memory){
        require(keccak256(abi.encode(password)) == keccak256(abi.encode(_password)));
        return flag;
    }
}