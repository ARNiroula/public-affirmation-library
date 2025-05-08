import React from 'react';

import {
  Card as MuiCard,
  CardProps as MuiCardProps
} from '@mui/material';

// Extend MUI Card props for your component
export interface CardProps extends MuiCardProps {
  // You can add custom props here if needed
}

const Card: React.FC<CardProps> = ({ children, ...props }) => {
  return (
    <MuiCard {...props}>
      {children}
    </MuiCard>
  );
};

export default Card;