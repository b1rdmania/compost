const { neon } = require('@neondatabase/serverless');

module.exports = async function handler(req, res) {
  // CORS headers
  res.setHeader('Access-Control-Allow-Origin', '*');
  res.setHeader('Access-Control-Allow-Methods', 'POST, OPTIONS');
  res.setHeader('Access-Control-Allow-Headers', 'Content-Type');

  if (req.method === 'OPTIONS') {
    return res.status(200).end();
  }

  if (req.method !== 'POST') {
    return res.status(405).json({ error: 'Method not allowed' });
  }

  const { email } = req.body;

  if (!email || !email.includes('@')) {
    return res.status(400).json({ error: 'Valid email required' });
  }

  try {
    const sql = neon(process.env.DATABASE_URL);

    // Create table if it doesn't exist
    await sql`
      CREATE TABLE IF NOT EXISTS waitlist (
        id SERIAL PRIMARY KEY,
        email VARCHAR(255) UNIQUE NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
      )
    `;

    // Insert email
    await sql`
      INSERT INTO waitlist (email)
      VALUES (${email.toLowerCase().trim()})
      ON CONFLICT (email) DO NOTHING
    `;

    return res.status(200).json({ success: true });
  } catch (error) {
    console.error('Waitlist error:', error);
    return res.status(500).json({ error: 'Something went wrong' });
  }
};
