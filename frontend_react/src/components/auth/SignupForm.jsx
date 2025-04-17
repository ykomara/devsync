// src/components/Auth/SignupForm.jsx
import React, { useState } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import { registerUser } from '../../features/auth/authSlice';

function SignupForm() {
  const dispatch = useDispatch();
  const { loading, error } = useSelector((state) => state.auth);

  const [formData, setFormData] = useState({
    email: '',
    full_name: '',
    password: '',
    role: 'DEV', // valeur par défaut
  });

  const handleChange = (e) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value
    });
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    dispatch(registerUser(formData));
  };

  return (
    <form onSubmit={handleSubmit} style={{ maxWidth: 400, margin: '0 auto' }}>
      <h2>Inscription</h2>

      <input
        type="email"
        name="email"
        placeholder="Adresse email"
        value={formData.email}
        onChange={handleChange}
        required
      /><br />

      <input
        type="text"
        name="full_name"
        placeholder="Nom complet"
        value={formData.full_name}
        onChange={handleChange}
        required
      /><br />

      <input
        type="password"
        name="password"
        placeholder="Mot de passe"
        value={formData.password}
        onChange={handleChange}
        required
      /><br />

      <select name="role" value={formData.role} onChange={handleChange}>
        <option value="DEV">Développeur</option>
        <option value="MANAGER">Manager</option>
        <option value="ADMIN">Admin</option>
      </select><br /><br />

      <button type="submit" disabled={loading}>
        {loading ? 'Inscription en cours...' : 'S’inscrire'}
      </button>

      {error && <p style={{ color: 'red' }}>{error}</p>}
    </form>
  );
}

export default SignupForm;
