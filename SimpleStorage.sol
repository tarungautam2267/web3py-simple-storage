//SPDX-License-Identifier: MIT
pragma solidity ^0.6.0;

contract SimpleStorage {
    uint256 favnumber;
    struct People {
        uint256 favnumber;
        string name;
    }
    People[] public people;

    mapping(string => uint256) public nameToFavnum;

    function store(uint256 _favnumber) public {
        favnumber = _favnumber;
    }

    function retrieve() public view returns (uint256) {
        return favnumber;
    }

    function addPerson(string memory _name, uint256 _favnumber) public {
        people.push(People(_favnumber, _name));
        nameToFavnum[_name] = _favnumber;
    }
}
