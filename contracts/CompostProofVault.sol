// SPDX-License-Identifier: MIT
pragma solidity ^0.8.24;

interface ICompostAsset {
    function transfer(address to, uint256 amount) external returns (bool);
    function transferFrom(address from, address to, uint256 amount) external returns (bool);
    function mint(address to, uint256 amount) external;
    function balanceOf(address account) external view returns (uint256);
}

contract CompostProofVault {
    string public constant name = "Compost Vault Share";
    string public constant symbol = "cHYPE";
    uint8 public constant decimals = 18;

    ICompostAsset public immutable asset;
    address public owner;

    uint256 public totalSupply;
    uint256 public totalManagedAssets;
    uint256 public aprBps;
    uint256 public lastAccrual;
    uint256 private unlocked = 1;

    mapping(address => uint256) public balanceOf;
    mapping(address => mapping(address => uint256)) public allowance;

    event Transfer(address indexed from, address indexed to, uint256 amount);
    event Approval(address indexed owner, address indexed spender, uint256 amount);
    event Deposit(address indexed caller, address indexed receiver, uint256 assets, uint256 shares);
    event Withdraw(address indexed caller, address indexed receiver, uint256 assets, uint256 shares);
    event Accrued(uint256 interestMinted, uint256 newTotalManagedAssets);
    event AprUpdated(uint256 oldAprBps, uint256 newAprBps);

    modifier onlyOwner() {
        require(msg.sender == owner, "OWNER_ONLY");
        _;
    }

    modifier nonReentrant() {
        require(unlocked == 1, "REENTRANCY");
        unlocked = 2;
        _;
        unlocked = 1;
    }

    constructor(address asset_, uint256 aprBps_) {
        require(asset_ != address(0), "ZERO_ASSET");
        require(aprBps_ <= 3_000, "APR_TOO_HIGH");

        owner = msg.sender;
        asset = ICompostAsset(asset_);
        aprBps = aprBps_;
        lastAccrual = block.timestamp;
    }

    function setAprBps(uint256 newAprBps) external onlyOwner {
        require(newAprBps <= 3_000, "APR_TOO_HIGH");
        _accrue();

        uint256 oldApr = aprBps;
        aprBps = newAprBps;

        emit AprUpdated(oldApr, newAprBps);
    }

    function accrue() external nonReentrant returns (uint256 interestMinted) {
        interestMinted = _accrue();
    }

    function _accrue() internal returns (uint256 interestMinted) {
        uint256 elapsed = block.timestamp - lastAccrual;
        if (elapsed == 0) return 0;

        lastAccrual = block.timestamp;

        uint256 principal = asset.balanceOf(address(this));
        totalManagedAssets = principal;

        if (principal == 0 || aprBps == 0) return 0;

        interestMinted = (principal * aprBps * elapsed) / (365 days * 10_000);

        if (interestMinted > 0) {
            asset.mint(address(this), interestMinted);
            totalManagedAssets = principal + interestMinted;
            emit Accrued(interestMinted, totalManagedAssets);
        }
    }

    function totalAssets() public view returns (uint256) {
        uint256 principal = asset.balanceOf(address(this));
        if (principal == 0 || aprBps == 0) return principal;

        uint256 elapsed = block.timestamp - lastAccrual;
        uint256 pending = (principal * aprBps * elapsed) / (365 days * 10_000);
        return principal + pending;
    }

    function pricePerShare() public view returns (uint256) {
        if (totalSupply == 0) return 1e18;
        return (totalAssets() * 1e18) / totalSupply;
    }

    function previewDeposit(uint256 assets) public view returns (uint256 shares) {
        if (totalSupply == 0) return assets;
        uint256 assetsBefore = totalAssets();
        if (assetsBefore == 0) return assets;
        return (assets * totalSupply) / assetsBefore;
    }

    function previewRedeem(uint256 shares) public view returns (uint256 assets) {
        if (totalSupply == 0) return 0;
        return (shares * totalAssets()) / totalSupply;
    }

    function deposit(uint256 assets, address receiver) external nonReentrant returns (uint256 shares) {
        require(assets > 0, "ZERO_ASSETS");
        require(receiver != address(0), "ZERO_RECEIVER");

        _accrue();
        shares = previewDepositWithAccrued(assets);
        require(shares > 0, "ZERO_SHARES");

        require(asset.transferFrom(msg.sender, address(this), assets), "TRANSFER_FROM_FAILED");
        totalManagedAssets = asset.balanceOf(address(this));
        _mint(receiver, shares);

        emit Deposit(msg.sender, receiver, assets, shares);
    }

    function redeem(uint256 shares, address receiver) external nonReentrant returns (uint256 assets) {
        require(shares > 0, "ZERO_SHARES");
        require(receiver != address(0), "ZERO_RECEIVER");
        require(balanceOf[msg.sender] >= shares, "INSUFFICIENT_SHARES");

        _accrue();
        uint256 assetsBefore = asset.balanceOf(address(this));
        assets = (shares * assetsBefore) / totalSupply;
        require(assets > 0, "ZERO_ASSETS");

        _burn(msg.sender, shares);
        require(asset.transfer(receiver, assets), "TRANSFER_FAILED");
        totalManagedAssets = asset.balanceOf(address(this));

        emit Withdraw(msg.sender, receiver, assets, shares);
    }

    function withdraw(uint256 assets, address receiver) external nonReentrant returns (uint256 shares) {
        require(assets > 0, "ZERO_ASSETS");
        require(receiver != address(0), "ZERO_RECEIVER");

        _accrue();
        shares = previewWithdrawWithAccrued(assets);
        require(balanceOf[msg.sender] >= shares, "INSUFFICIENT_SHARES");

        _burn(msg.sender, shares);
        require(asset.transfer(receiver, assets), "TRANSFER_FAILED");
        totalManagedAssets = asset.balanceOf(address(this));

        emit Withdraw(msg.sender, receiver, assets, shares);
    }

    function previewDepositWithAccrued(uint256 assets) internal view returns (uint256 shares) {
        if (totalSupply == 0) return assets;
        uint256 assetsBefore = asset.balanceOf(address(this));
        if (assetsBefore == 0) return assets;
        return (assets * totalSupply) / assetsBefore;
    }

    function previewWithdrawWithAccrued(uint256 assets) internal view returns (uint256 shares) {
        uint256 assetsBefore = asset.balanceOf(address(this));
        require(assetsBefore > 0, "ZERO_ASSETS");
        shares = (assets * totalSupply) / assetsBefore;
        if ((shares * assetsBefore) / totalSupply < assets) {
            shares += 1;
        }
    }

    function approve(address spender, uint256 amount) external returns (bool) {
        allowance[msg.sender][spender] = amount;
        emit Approval(msg.sender, spender, amount);
        return true;
    }

    function transfer(address to, uint256 amount) external returns (bool) {
        _transfer(msg.sender, to, amount);
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

    function _burn(address from, uint256 amount) internal {
        require(from != address(0), "ZERO_ADDRESS");
        require(balanceOf[from] >= amount, "BALANCE");

        unchecked {
            balanceOf[from] -= amount;
            totalSupply -= amount;
        }

        emit Transfer(from, address(0), amount);
    }
}
