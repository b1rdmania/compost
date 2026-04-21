const hre = require("hardhat");

async function main() {
  const aprBps = 1000; // 10.00%

  const [deployer] = await hre.ethers.getSigners();
  console.log("Deployer:", deployer.address);

  const MockHype = await hre.ethers.getContractFactory("MockHype");
  const mockHype = await MockHype.deploy();
  await mockHype.waitForDeployment();

  const CompostProofVault = await hre.ethers.getContractFactory("CompostProofVault");
  const vault = await CompostProofVault.deploy(await mockHype.getAddress(), aprBps);
  await vault.waitForDeployment();

  const tx = await mockHype.setMinter(await vault.getAddress(), true);
  await tx.wait();

  console.log("MockHype:", await mockHype.getAddress());
  console.log("CompostProofVault:", await vault.getAddress());
  console.log("APR (bps):", aprBps);
}

main().catch((error) => {
  console.error(error);
  process.exitCode = 1;
});
