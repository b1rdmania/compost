const { expect } = require("chai");
const { ethers } = require("hardhat");

describe("CompostProofVault", function () {
  async function deployFixture() {
    const [owner, user, other] = await ethers.getSigners();

    const MockHype = await ethers.getContractFactory("MockHype");
    const token = await MockHype.deploy();
    await token.waitForDeployment();

    const CompostProofVault = await ethers.getContractFactory("CompostProofVault");
    const vault = await CompostProofVault.deploy(await token.getAddress(), 1000); // 10%
    await vault.waitForDeployment();

    await (await token.setMinter(await vault.getAddress(), true)).wait();
    await (await token.mint(user.address, ethers.parseUnits("5000", 18))).wait();
    await (await token.connect(user).approve(await vault.getAddress(), ethers.MaxUint256)).wait();

    return { owner, user, other, token, vault };
  }

  it("uses on-chain symbols aligned with UI", async function () {
    const { token, vault } = await deployFixture();
    expect(await token.symbol()).to.equal("vHYPE");
    expect(await vault.symbol()).to.equal("cHYPE");
  });

  it("supports deposit and withdraw roundtrip", async function () {
    const { user, token, vault } = await deployFixture();
    const depositAmount = ethers.parseUnits("1000", 18);

    await (await vault.connect(user).deposit(depositAmount, user.address)).wait();

    const shares = await vault.balanceOf(user.address);
    expect(shares).to.equal(depositAmount);

    await (await vault.connect(user).withdraw(ethers.parseUnits("250", 18), user.address)).wait();

    const remainingShares = await vault.balanceOf(user.address);
    expect(remainingShares).to.be.lt(shares);
    expect(await token.balanceOf(user.address)).to.be.gte(ethers.parseUnits("4250", 18));
  });

  it("increases share price over time after accrue", async function () {
    const { user, vault } = await deployFixture();
    const depositAmount = ethers.parseUnits("1000", 18);

    await (await vault.connect(user).deposit(depositAmount, user.address)).wait();

    const before = await vault.pricePerShare();

    await ethers.provider.send("evm_increaseTime", [30 * 24 * 60 * 60]);
    await ethers.provider.send("evm_mine", []);

    await (await vault.connect(user).accrue()).wait();

    const after = await vault.pricePerShare();
    expect(after).to.be.gt(before);
  });

  it("accounts for direct token transfers into the vault", async function () {
    const { user, other, token, vault } = await deployFixture();
    const depositAmount = ethers.parseUnits("1000", 18);

    await (await vault.connect(user).deposit(depositAmount, user.address)).wait();

    await (await token.mint(other.address, ethers.parseUnits("100", 18))).wait();
    await (await token.connect(other).transfer(await vault.getAddress(), ethers.parseUnits("100", 18))).wait();

    const assets = await vault.totalAssets();
    expect(assets).to.be.gte(ethers.parseUnits("1100", 18));
  });
});
