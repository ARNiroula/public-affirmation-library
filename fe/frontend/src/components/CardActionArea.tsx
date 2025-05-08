import React from 'react';
import { CardActionArea as MuiCardActionArea, CardActionAreaProps } from '@mui/material';

const CardActionArea: React.FC<CardActionAreaProps> = ({ children, ...props }) => {
  return <MuiCardActionArea {...props}>{children}</MuiCardActionArea>;
};

export default CardActionArea;
