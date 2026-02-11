// SPDX-License-Identifier: MIT
pragma solidity ^0.8.24;

contract MockHype {
    string public constant name = "Vault HYPE";
    string public constant symbol = "vHYPE";
    uint8 public constant decimals = 18;

    uint256 public totalSupply;
    address public owner;

    mapping(address => uint256) public balanceOf;
    mapping(address => mapping(address => uint256)) public allowance;
    mapping(address => bool) public minters;
    mapping(address => uint256) public lastDripAt;

    uint256 public constant DRIP_AMOUNT = 1_000 ether;
    uint256 public constant DRIP_COOLDOWN = 12 hours;

    event Transfer(address indexed from, address indexed to, uint256 amount);
    event Approval(address indexed owner, address indexed spender, uint256 amount);
    event MinterSet(address indexed account, bool allowed);

    modifier onlyOwner() {
        require(msg.sender == owner, "OWNER_ONLY");
        _;
    }

    modifier onlyMinter() {
        require(minters[msg.sender], "MINTER_ONLY");
        _;
    }

    constructor() {
        owner = msg.sender;
        minters[msg.sender] = true;
    }

    function setMinter(address account, bool allowed) external onlyOwner {
        minters[account] = allowed;
        emit MinterSet(account, allowed);
    }

    function drip() external {
        require(block.timestamp >= lastDripAt[msg.sender] + DRIP_COOLDOWN, "DRIP_COOLDOWN");
        lastDripAt[msg.sender] = block.timestamp;
        _mint(msg.sender, DRIP_AMOUNT);
    }

    function mint(address to, uint256 amount) external onlyMinter {
        _mint(to, amount);
    }

    function transfer(address to, uint256 amount) external returns (bool) {
        _transfer(msg.sender, to, amount);
        return true;
    }

    function approve(address spender, uint256 amount) external returns (bool) {
        allowance[msg.sender][spender] = amount;
        emit Approval(msg.sender, spender, amount);
        return true;
    }

    function transferFrom(address from, address to, uint256 amount) external returns (bool) {
        uint256 allowed = allowance[from][msg.sender];
        require(allowed >= amount, "ALLOWANCE");

        if (allowed != type(uint256).max) {
            allowance[from][msg.sender] = allowed - amount;
            emit Approval(from, msg.sender, allowance[from][msg.sender]);
        }

        _transfer(from, to, amount);
        return true;
    }

    function _transfer(address from, address to, uint256 amount) internal {
        require(to != address(0), "ZERO_ADDRESS");
        require(balanceOf[from] >= amount, "BALANCE");

        unchecked {
            balanceOf[from] -= amount;
            balanceOf[to] += amount;
        }

        emit Transfer(from, to, amount);
    }

    function _mint(address to, uint256 amount) internal {
        require(to != address(0), "ZERO_ADDRESS");

        totalSupply += amount;
        balanceOf[to] += amount;

        emit Transfer(address(0), to, amount);
    }
}
