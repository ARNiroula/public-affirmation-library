import React from 'react';
import { Typography as MuiTypography, TypographyProps } from '@mui/material';

const Typography: React.FC<TypographyProps> = ({ children, ...props }) => {
  return <MuiTypography {...props}>{children}</MuiTypography>;
};

export default Typography;
