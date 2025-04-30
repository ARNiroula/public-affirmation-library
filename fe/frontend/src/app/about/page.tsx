import React from 'react';

const AboutPage: React.FC = () => {
  return (
    <div style={styles.container}>
      <header style={styles.header}>
        <h1>About PAL</h1>
      </header>
      <main style={styles.main}>
        <section style={styles.section}>
          <h2>Our Mission</h2>
          <p>
            PAL (Public Affirmation Library) is dedicated to serving the community by providing access to diversified resources, affordable rental services, free study room reservations, and hosting educational events on a wide range of topics.
          </p>
        </section>
        <section style={styles.section}>
          <h2>What We Do</h2>
          <ul>
            <li>Maintain a rich inventory of books across various topics.</li>
            <li>Organize engaging events, including seminars and exhibitions.</li>
            <li>Offer free study room reservations for groups.</li>
            <li>Support customers with convenient rental and payment options.</li>
          </ul>
        </section>
        <section style={styles.section}>
          <h2>Why Choose Us</h2>
          <p>
            At PAL, we believe in empowering individuals and groups through education and collaboration. By transitioning to a sophisticated centralized database system, we ensure that our services remain efficient, reliable, and accessible to everyone.
          </p>
        </section>
      </main>
      <footer style={styles.footer}>
        <p>&copy; 2025 Public Affirmation Library. All rights reserved.</p>
      </footer>
    </div>
  );
};

const styles: Record<string, React.CSSProperties> = {
  container: {
    fontFamily: 'Arial, sans-serif',
    lineHeight: '1.6',
    color: '#333',
    display: 'flex',
    flexDirection: 'column',
    minHeight: '100vh',
  },
  header: {
    backgroundColor: '#007BFF',
    color: '#fff',
    padding: '20px',
    textAlign: 'center',
  },
  main: {
    flex: 1,
    padding: '20px',
  },
  section: {
    marginBottom: '20px',
    padding: '10px',
    border: '1px solid #ddd',
    borderRadius: '5px',
    backgroundColor: '#f9f9f9',
  },
  footer: {
    textAlign: 'center',
    padding: '10px',
    backgroundColor: '#f1f1f1',
  },
};

export default AboutPage;