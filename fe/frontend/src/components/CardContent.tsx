import React from 'react';
import { CardContent as MuiCardContent, CardContentProps } from '@mui/material';

const CardContent: React.FC<CardContentProps> = (props) => {
  return <MuiCardContent {...props} />;
};

export default CardContent;
