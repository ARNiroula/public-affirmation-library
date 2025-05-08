import React from 'react';
import { CardMedia as MuiCardMedia, CardMediaProps } from '@mui/material';

const CardMedia: React.FC<CardMediaProps> = (props) => {
  return <MuiCardMedia {...props} />;
};

export default CardMedia;
